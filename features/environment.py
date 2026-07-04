from services.bank_account.bank_account_services import BankAccountService
from services.user.user_services import UserService
from repositories.user_repository import UserRepository
from models.user import User
from models.bank_account import BankAccount
from DB.db import session

def before_scenario(context, scenario):
    db = session()

    db.query(User).delete()
    db.query(BankAccount).delete()
    db.commit()

    context.user_service = UserService(UserRepository(db))
    context.bank_account_service = BankAccountService(UserRepository(db))