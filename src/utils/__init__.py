# Arquivo para guardar pedaços de código que são repetidos em vários lugares do projeto.

from models import engine, DataEvento, Relevancia, TipoEvento
from sqlalchemy import select, asc
from typing import Sequence

def get_relevancy_levels():
    # Função para retornar os dados de relevância dos eventos -> Alto, baixo, médio
    with engine.connect() as conn:
        niveis_relevancia: Sequence[Relevancia] = conn.execute(
            select(Relevancia)
        ).scalars().all()
    return niveis_relevancia


def get_event_types():
    # Função para retornar os tipos de eventos -> Prova, trabalho, apresentação, etc.
    with engine.connect() as conn:
        tipo_eventos: Sequence[TipoEvento] = conn.execute(
            select(TipoEvento)
        ).scalars().all()
    return tipo_eventos


def get_user_events(user_id):
    # Função para retornar os eventos de um usuário (no caso, seria o que está logado).
    # Os dados são retornados de forma ascendente pela data do evento (o mais antigo vem primeiro).
    with engine.connect() as conn:
        datas: Sequence[DataEvento] = conn.execute(
            select(DataEvento).where(DataEvento.user_id == user_id).order_by(asc(DataEvento.data))
        ).scalars().all()
    return datas


'''def make_session():
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    return Session()'''
# preciso verificar como funcionaria essa função no código e se ela tá certa