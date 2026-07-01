import unittest
import datetime

from common.transaction_type import TransactionType
from services.transaction.transaction_services import TransactionService


class TestTransactionService(unittest.TestCase):
    def setUp(self):
        self.transaction = TransactionDouble(
            id = '12' ,
            account_id = '123',
            transaction_type = TransactionType.DEPOSIT,
            amount = 1000,
            date = datetime.datetime.now)
        self.transaction_repository = TransactionRepositorySpy()
        self.transaction_service = TransactionService(self.transaction_repository)


    def test_create_transaction(self):
        transaction = self.transaction_service.create_transaction(self.transaction)
        self.assertEqual(self.transaction , transaction)

class TransactionRepositorySpy:
    def __init__(self):
        self.transaction = None

    def create_transaction(self , transaction):
        self.transaction = transaction
        return transaction


class TransactionDouble:
    def __init__(self, id = '12' ,
                 account_id = '123',
                 transaction_type = TransactionType.DEPOSIT,
                 amount = 1000,
                 date = datetime.datetime.now):
        self.id = id
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = date
