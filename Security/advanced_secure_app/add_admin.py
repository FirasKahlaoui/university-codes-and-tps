from app import create_app
from app.extensions import db
from app.models import Admin

def add_admin(username, email, password):
    app = create_app()
    with app.app_context():
        admin = Admin(username=username, email=email)
        admin.set_password(password)
        db.session.add(admin)
        db.session.commit()
        print(f"Admin user {username} added successfully!")

if __name__ == "__main__":
    username = "admin"
    email = "kahlaoui@gmail.com"
    password = "topadmin"
    add_admin(username, email, password)