from typing import List, Optional

from models.transaction import Transaction
from exceptions.transaction_exceptions import TransactionNotFound, InsufficientBalance


class TransactionService:
    def __init__(self , transaction_repository):
        self.transaction_repository = transaction_repository

    def create_transaction(self, transaction:Transaction)->Transaction:
        if transaction.amount < 0:
            raise ValueError('amount must be greater than zero')
        self.transaction_repository.create_transaction(transaction)
        return transaction

    def get_all_transactions(self)->List[Transaction]:
        return self.transaction_repository.get_all_transactions()

    def get_transaction_by_id(self, transaction_id:str)->Optional[Transaction]:
        transaction = self.transaction_repository.get_transaction_by_id(transaction_id)
        if transaction is None:
            raise TransactionNotFound(f'Transaction not found with id: {transaction_id}')
        return self.transaction_repository.get_transaction_by_id(transaction.id)

    def get_transaction_by_account_id(self, account_id:str)->Optional[Transaction]:
        transaction = self.transaction_repository.get_transaction_by_account_id(account_id)
        if transaction is None:
            raise TransactionNotFound(f'Transaction not found with account id: {account_id}')
        return self.transaction_repository.get_transaction_by_account_id(account_id)

    def update_transaction(self, transaction:Transaction)->Transaction | None:
        if self.get_transaction_by_id(transaction.id):
            self.transaction_repository.update_transaction(transaction)
            return transaction
        return None

    def delete_transaction(self, transaction:Transaction)->Transaction | None:
        if self.get_transaction_by_id(transaction.id):
            self.transaction_repository.delete_transaction(transaction)
            return transaction
        return None