from app import create_app
from app.extensions import db, bcrypt
from app.models import Admin


def add_admin(username, email, password):
    app = create_app()
    with app.app_context():
        hashed_password = bcrypt.generate_password_hash(
            password).decode('utf-8')
        admin = Admin(username=username, email=email, password=hashed_password)
        db.session.add(admin)
        db.session.commit()
        print(f"Admin user {username} added successfully!")


if __name__ == "__main__":
    username = "admin"
    email = "kahlaoui@gmail.com"
    password = "topadmin"
    add_admin(username, email, password)
