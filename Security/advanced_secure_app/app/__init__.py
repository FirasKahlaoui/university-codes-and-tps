from flask import Flask
from config import Config
from app.extensions import db, mail, bcrypt, login_manager
from app.routes import main
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


def create_app(config_class=Config):
    # Print debug information
    print("Current Working Directory:", os.getcwd())
    print("Template Folder Path:", os.path.join(os.getcwd(), 'templates'))

    # Create Flask app instance
    app = Flask(__name__, template_folder='templates',
                static_folder='app/static')
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
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
