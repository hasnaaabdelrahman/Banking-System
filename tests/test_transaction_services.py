import unittest
import datetime
from assertpy import assert_that

from common.transaction_type import TransactionType
from exceptions.transaction_exceptions import TransactionNotFound
from services.transaction.transaction_services import TransactionService


class TestTransactionService(unittest.TestCase):
    def setUp(self):
        self.transaction = TransactionDouble(id = '12' ,account_id = '123',transaction_type = TransactionType.DEPOSIT,amount = 1000,date = datetime.datetime.now)
        self.transaction_repository = TransactionRepositorySpy()
        self.transaction_service = TransactionService(self.transaction_repository)


    def test_create_transaction(self):
        transaction = self.transaction_service.create_transaction(self.transaction)
        assert_that(self.transaction).is_equal_to(transaction)

    def test_get_all_transactions(self):
        transactions = self.transaction_service.get_all_transactions()
        assert_that(len(transactions), 2)

    def test_get_transaction_by_id(self):
        self.transaction_repository.transaction = self.transaction
        transaction = self.transaction_service.get_transaction_by_id(self.transaction.id)
        assert_that(self.transaction).is_equal_to(transaction)

    def test_get_transaction_by_account_id(self):
        self.transaction_repository.transaction = self.transaction
        transactions = self.transaction_service.get_transaction_by_account_id(self.transaction.account_id)
        assert_that(self.transaction).is_equal_to(transactions)

    def test_update_transaction(self):
        self.transaction_repository.transaction = self.transaction
        transaction = self.transaction_service.update_transaction(self.transaction)
        assert_that(self.transaction).is_equal_to(transaction)

    def test_delete_transaction(self):
        self.transaction_repository.transaction = self.transaction
        transaction = self.transaction_service.delete_transaction(self.transaction)
        assert_that(self.transaction).is_equal_to(transaction)

    def test_transaction_not_found_will_raise_exception(self):
        with self.assertRaises(TransactionNotFound):
            self.transaction_service.get_transaction_by_id(self.transaction.id)

    def test_transaction_not_found_by_account_id_will_raise_exception(self):
        with self.assertRaises(TransactionNotFound):
            self.transaction_service.get_transaction_by_account_id(self.transaction.account_id)


class TransactionRepositorySpy:
    def __init__(self):
        self.transaction = None
        self.transactions_list =[]

    def create(self , transaction):
        if transaction.amount < 0:
            return None
        return transaction

    def get_all_transactions(self):
        return self.transactions_list

    def get_by_id(self , id):
        if self.transaction and self.transaction.id == id:
            return self.transaction
        return None

    def get_by_account_id(self , account_id):
        if self.transaction and self.transaction.account_id == account_id:
            return self.transaction
        return None

    def update(self , transaction):
        if self.transaction:
            return self.transaction
        return transaction

    def delete(self , transaction):
        if self.transaction:
            return self.transaction
        return None

class TransactionDouble:
    def __init__(self, id = '12' ,account_id = '123',transaction_type = TransactionType.DEPOSIT,amount = 1000,date = datetime.datetime.now):
        self.id = id
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = date
