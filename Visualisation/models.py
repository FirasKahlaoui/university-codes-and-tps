from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
    education_level = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

# Create an engine that stores data in the local directory's sqlite database file.
engine = create_engine('sqlite:///app.db')

# Create all tables in the engine.
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()