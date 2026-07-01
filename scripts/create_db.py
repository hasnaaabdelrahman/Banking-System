from DB.db import Base, engine

from models.user import User
from models.bank_account import BankAccount
from models.transaction import Transaction

Base.metadata.create_all(bind=engine)