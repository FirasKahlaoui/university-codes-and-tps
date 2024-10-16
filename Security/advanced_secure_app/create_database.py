from app import create_app
from app.extensions import db
from app.models import Admin, User, Log

def create_db():
    app = create_app()
    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Database and tables created successfully!")

if __name__ == "__main__":
    create_db()