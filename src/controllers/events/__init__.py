from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import User, TipoEvento, Relevancia, DataEvento
from models import engine
from sqlalchemy import select, desc
from sqlalchemy.orm import Session
import utils

events_bp = Blueprint('events', __name__, template_folder='templates', static_folder='static')

# TEM QUE AJEITAR TUDO DESSA ROTA

@events_bp.route('/events')
@login_required
def events():
    # Página de visualização dos eventos. Será disposto no HTML como cards de datas, onde a ordem será do mais próximo ao mais distante.
    with Session(engine) as session:
        # datas = session.query(DataEvento).filter(DataEvento.user_id == current_user.id).order_by(desc(DataEvento.data)).all()
        datas_usuario = (
            select(
                DataEvento.id,
                DataEvento.titulo_evento,
                DataEvento.data,
                Relevancia.nivel.label("relevancia"),
                TipoEvento.nome.label("tipo_evento"),
            )
            .join(Relevancia, DataEvento.relevancia_id == Relevancia.id)
            .join(TipoEvento, DataEvento.tipo_evento_id == TipoEvento.id)
            .filter(DataEvento.user_id == current_user.id)
        )

        datas = session.execute(datas_usuario).all()
    return render_template('events.html', datas=datas)

@events_bp.route('/events/add', methods=['GET', 'POST'])
@login_required
def events_add():
    if request.method == 'POST':
        titulo_evento = request.form.get('titulo_evento')
        data = request.form.get('data')
        relevancia_id = request.form.get('relevancia_id')
        tipo_evento_id = request.form.get('tipo_evento_id')

        with engine.connect() as conn:
            try:
                session = Session(engine)
                new_event = DataEvento(
                    titulo_evento=titulo_evento,
                    data=data,
                    user_id=current_user.id,
                    relevancia_id=relevancia_id,
                    tipo_evento_id=tipo_evento_id
                )

                session.add(new_event)
                session.commit()
                session.close()
                
                flash("Data adicionada com sucesso!", category='success')
                return redirect(url_for('events.events'))
            
            except Exception as e:
                flash("Não foi possível adicionar a data. Tente novamente.", category="error")

    if request.method == "GET":
        niveis_relevancia = utils.get_relevancy_levels()
        tipo_eventos = utils.get_event_types()
        
        return render_template('events_add.html', 
                niveis_relevancia=niveis_relevancia,
                tipo_eventos=tipo_eventos)



@events_bp.route('/events/delete/<int:event_id>', methods=['POST'])
@login_required
def events_delete(event_id):
    with engine.connect() as conn:
        try:
            session = Session(engine)
            event_delete = session.get(DataEvento, event_id)
            session.delete(event_delete)
            session.commit()
            session.close()
            flash("Data deletada com sucesso!", category='success')
            return redirect(url_for('events.events'))
        except Exception as e:
            flash("Não foi possível deletar a data. Tente novamente.", category="error")
            return redirect(url_for('events.events'))



@events_bp.route('/events/edit/<int:event_id>', methods=['GET', 'POST'])
@login_required
def events_edit(event_id):
    if request.method == "POST":
        titulo_evento = request.form.get('titulo_evento')
        data = request.form.get('data')
        relevancia_id = request.form.get('relevancia_id')
        tipo_evento_id = request.form.get('tipo_evento_id')

        with engine.connect() as conn:
            try:
                session = Session(engine)
                event_edit = session.query(DataEvento).where(DataEvento.id == event_id).first()
                event_edit.titulo_evento = titulo_evento
                event_edit.data = data
                event_edit.relevancia_id = relevancia_id
                event_edit.tipo_evento_id = tipo_evento_id

                session.commit()
                session.close()
                
                flash("Data editada com sucesso!", category='success')
                return redirect(url_for('events.events'))
            
            except Exception as e:
                flash("Não foi possível editar a data. Tente novamente.", category="error")
                return redirect(url_for('events.events'))
    
    if request.method == "GET":
        with Session(engine) as session:
            event = session.query(DataEvento).filter(DataEvento.id == event_id).first() 
            
            niveis_relevancia = utils.get_relevancy_levels()
            tipo_eventos = utils.get_event_types()
        
        return render_template('events_edit.html', 
                event=event,
                niveis_relevancia=niveis_relevancia,
                tipo_eventos=tipo_eventos)