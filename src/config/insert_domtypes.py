from models import Relevancia, TipoEvento
from sqlalchemy.orm import Session


def insert_relevancia(engine):
    with Session(engine) as session:
        niveis_relevancia: list[Relevancia] = [
            Relevancia(nivel="Baixa"),
            Relevancia(nivel="Média"),
            Relevancia(nivel="Alta"),
        ]

        session.add_all(niveis_relevancia)
        session.commit()

def insert_tipo_evento(engine):
    with Session(engine) as session:
        tipos_evento: list[TipoEvento] = [
            TipoEvento(nome="Prova"),
            TipoEvento(nome="Trabalho"),
            TipoEvento(nome="Projeto"),
        TipoEvento(nome="Seminário")
        ]

    session.add_all(tipos_evento)
    session.commit()