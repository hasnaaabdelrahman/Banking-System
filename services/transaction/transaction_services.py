from typing import List, Optional

from models.transaction import Transaction


class TransactionService:
    def __init__(self , transaction_repository):
        self.transaction_repository = transaction_repository

    def create_transaction(self, transaction:Transaction)->Transaction:
        self.transaction_repository.create_transaction(transaction)
        return transaction

    def get_all_transactions(self)->List[Transaction]:
        return self.transaction_repository.get_all_transactions()

    def get_transaction_by_id(self, transaction_id:str)->Optional[Transaction]:
        return self.transaction_repository.get_transaction_by_id(transaction_id)
