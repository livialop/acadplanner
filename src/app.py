from flask import Flask
from controllers.auth import auth_bp
from controllers.error import error_bp
from controllers.main import main_bp
from controllers.events import events_bp
from config.config_app import config, start_database


app: Flask = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(error_bp)
app.register_blueprint(events_bp)

config(app)

if __name__ == "__main__":
    start_database(app) # Criação do banco de dados
