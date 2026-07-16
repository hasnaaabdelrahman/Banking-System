from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DATABASE_URL = "sqlite:///bank.db"

engine = create_engine(DATABASE_URL , echo=True) # connect app with db
Session = sessionmaker(bind=engine) # commit
session = Session()

class Base(DeclarativeBase): # all classes will inherit from
    pass

