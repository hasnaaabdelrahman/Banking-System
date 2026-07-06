from typing import Optional

from sqlalchemy.exc import SQLAlchemyError


from models.transaction import Transaction

class TransactionRepository:
    def __init__(self, session):
        self.session = session

    def get_all(self) -> list[Transaction]:
        return self.session.query(Transaction).all()

    def get_by_id(self , id:str) -> Optional[Transaction]:
        return self.session.query(Transaction).filter_by(id = id).first()

    def get_by_account_id(self, account_id: str) -> list[Transaction]:
        return self.session.query(Transaction).filter_by(account_id = account_id).all()

    def create(self , transaction: Transaction) ->Transaction:
        try:
            self.session.add(transaction)
            self.session.commit()
            self.session.refresh(transaction)
            return transaction
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def update(self, transaction: Transaction) -> Transaction:
        try:
            self.session.commit()
            self.session.refresh(transaction)
            return transaction
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def delete(self, transaction: Transaction) -> Transaction:
        try:
            self.session.delete(transaction)
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()
            raise