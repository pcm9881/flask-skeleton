from flask import Flask, request, g
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
import logging

migrate = Migrate()
db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'
mail = Mail()
migrate = Migrate()

def create_app():
    logging.basicConfig(filename='logs/record.log', level=logging.DEBUG)
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
