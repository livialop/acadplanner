from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from models import engine, User
from sqlalchemy.orm import Session
from sqlalchemy import select
from werkzeug.security import generate_password_hash, check_password_hash

user_bp = Blueprint('user', __name__, template_folder='templates', static_folder='static')

@user_bp.route('/user')
@login_required
def user():
    # Página de visualização das informações do usuário
    with Session(engine) as session:
        user_info = (
            select(
                User.name,
                User.username,
                User.email,
                User.password
            )
            .filter(User.id == current_user.id)
        )

        informacoes = session.execute(user_info).all()

    return render_template('user.html',
                           informacoes=informacoes)


@user_bp.route('/user/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user_edit(user_id: int):
    # Rota para atualizar os dados de um usuário.
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        # Pede a senha atual primeiro para checar as informações mudadas.
        actual_password = request.form.get('actual_password')
        # Caso troque de senha. Se o usuário deixar nulo, a mesma senha é mantida.
        new_password = request.form.get('new_password')

        with Session(engine) as session:
            try:
                user_db = session.query(User).filter(User.id == current_user.id).first()
                
                # Verifica se o username é de outro usuário.
                verify_username = session.query(User).filter(User.username == username, User.id != current_user.id).first()
                if verify_username:
                    flash('Esse username já está cadastrado. Escolha outro, por favor.', category='error')
                    return redirect(url_for('user.user_edit', user_id=current_user.id))
                
                verify_email = session.query(User).filter(User.email == email, User.id != current_user.id).first()
                if verify_email:
                    flash('Esse email já está cadastrado. Por favor, escolha outro.', category='error')
                    return redirect(url_for('user.user_edit', user_id=current_user.id))
                
                if not check_password_hash(user_db.password, actual_password):
                    flash('Senha incorreta.', category='error')
                    return redirect(url_for('user.user_edit', user_id=current_user.id))
                
                if check_password_hash(user_db.password, actual_password):
                    user_db.name = name
                    user_db.username = username
                    user_db.email = email
                    
                    # Se o usuário tiver mudado o campo de senha
                    if new_password and new_password.strip() != "":
                        user_db.password = generate_password_hash(new_password)
                    # Caso não tenha mudado, a senha permanece.
                    session.commit()

                    flash('Informações editadas com sucesso!', category='success')
                    return redirect(url_for('user.user'))
            except Exception as e:
                session.rollback()
                print("Erro ao editar usuário:", e)
                flash('Ocorreu um erro ao atualizar suas informações.', category='error')
                return redirect(url_for('user.user'))
                
    if request.method == 'GET':
        # Se a request for GET, ele pega todas as informações do usuário logado no momento e retorna para o front
        with Session(engine) as session:
            user_info = session.query(User).filter(User.id == current_user.id).first()

        return render_template('user_edit.html',
                               user_info=user_info)