from flask import Flask
from app.extensions import db, bcrypt, login_manager
from app.routes import main

def create_app():
    import os
    print("Current Working Directory:", os.getcwd())
    print("Template Folder Path:", os.path.join(os.getcwd(), 'templates'))

    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(main)

    return app