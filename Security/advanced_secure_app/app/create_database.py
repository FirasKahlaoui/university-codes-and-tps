from app import create_app, db


def create_db():
    app = create_app()
    with app.app_context():
        try:
            print("Creating tables...")
            db.create_all()
            print("Database and tables created successfully!")
        except Exception as e:
            print(f"Error creating database: {e}")
            raise


if __name__ == "__main__":
    create_db()
