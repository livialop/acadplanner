from models import DataEvento, session


datas_eventos = session.query(DataEvento).all()
print(datas_eventos)