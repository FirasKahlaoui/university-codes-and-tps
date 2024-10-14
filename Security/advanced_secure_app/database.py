from extensions import db
from models import Admin, User, Log

def create_db():
    db.create_all()