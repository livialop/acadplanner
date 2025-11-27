from config.insert_domtypes import insert_relevancia, insert_tipo_evento
from models import engine, Base, User, Relevancia, TipoEvento
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager
from flask import Flask

def config(app: Flask) -> None:
    app.secret_key = 'LASJDHJDWUABBDAWDB@##'

    login_manager: LoginManager = LoginManager(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id) -> User | None:
        Session = sessionmaker(bind=engine)
        with Session() as session:
            return session.get(User, int(user_id))


def start_database(app) -> None:
    with app.app_context():
        Base.metadata.create_all(engine)
        # Inserindo dados das tabelas de domínio, se não existirem
        Session = sessionmaker(bind=engine)
        with Session() as session:
            if not session.query(Relevancia).first():
                insert_relevancia(engine)
            if not session.query(TipoEvento).first():
                insert_tipo_evento(engine)

    app.run(debug=True)