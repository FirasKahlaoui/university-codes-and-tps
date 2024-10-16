from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config
from app.extensions import db, bcrypt, login_manager
from app.routes import main
import logging
from logging.handlers import RotatingFileHandler
import os

mail = Mail()


def create_app(config_class=Config):
    print("Current Working Directory:", os.getcwd())
    print("Template Folder Path:", os.path.join(os.getcwd(), 'templates'))

    app = Flask(__name__, template_folder='templates',
                static_folder='app/static')
    app.config.from_object(config_class)

    db.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(main)

    # Configure logging
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler(
        'logs/app.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Advanced Secure App startup')

    return app
