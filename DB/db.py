from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DATABASE_URL = "sqlite:///bank.db"

engine = create_engine(DATABASE_URL , echo=True) # connect app with db
session = sessionmaker(bind=engine) # commit

class Base(DeclarativeBase): # all classes will inherit from
    pass

