from services.bank_account.bank_account_services import BankAccountService
from services.transaction.transaction_services import TransactionService
from services.user.user_services import UserService
from repositories.user_repository import UserRepository
from repositories.bank_account_repository import BankAccountRepository
from repositories.transaction_repository import TransactionRepository
from models.user import User
from models.bank_account import BankAccount
from models.transaction import Transaction
from Database.db import session

def before_scenario(context, scenario):
    db = session()

    db.query(User).delete()
    db.query(BankAccount).delete()
    db.query(Transaction).delete()
    db.commit()

    context.user_service = UserService(UserRepository(db))
    context.bank_account_service = BankAccountService(BankAccountRepository(db))
    context.transaction_service = TransactionService(TransactionRepository(db))