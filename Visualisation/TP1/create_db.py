from Visualisation.TP1.models import Base, engine

# Create all tables in the engine.
Base.metadata.create_all(engine)

print("Database and tables created successfully!")