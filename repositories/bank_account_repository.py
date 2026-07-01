from typing import Optional
from sqlalchemy.exc import SQLAlchemyError
from models.bank_account import BankAccount

class BankAccountRepository:
    def __init__(self , session):
        self.session = session

    def get_by_id(self , id:str) -> Optional[BankAccount]:
        return self.session.query(BankAccount).filter_by(id = id).first()

    def get_by_user_id(self , user_id:str) -> Optional[BankAccount]:
        return self.session.query(BankAccount).filter_by(user_id = user_id).first()

    def create(self , bank_account:BankAccount) -> BankAccount:
        try:
            self.session.add(bank_account)
            self.session.commit()
            self.session.refresh(bank_account)
            return bank_account
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def update(self , bank_account:BankAccount) -> BankAccount:
        try:
            self.session.commit()
            self.session.refresh(bank_account)
            return bank_account
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def delete(self , id:str) -> bool:
        try:
            bank_account = self.get_by_id(id)
            if bank_account is None:
                return False
            self.session.delete(bank_account)
            self.session.commit()
            return True
        except SQLAlchemyError:
            self.session.rollback()
            raise

