import unittest

from common.account_type import AccountType
from exceptions.bank_account_exceptions import BankAccountAlreadyExists, BankAccountNotFound
from repositories.bank_account_repository import BankAccountRepository
from services.bank_account.bank_account_services import BankAccountService

class TestBankAccountService(unittest.TestCase):
    def setUp(self):
        self.bank_account = BankAccountDouble(
            id = '123',
            account_number='123456789',
            account_type=AccountType.SAVINGS,
            balance=1000,
            is_active=True,
            user_id='1'
        )
        self.bank_account_repository = BankAccountRepositorySpy()
        self.bank_account_services = BankAccountService(self.bank_account_repository)

    def test_create_bank_account(self):
        account = self.bank_account_services.create_bank_account(self.bank_account)
        self.assertEqual(self.bank_account , account)
        self.assertEqual(self.bank_account_repository.bank_account.id , '123')

    def test_bank_account_already_exists_will_raises_exception(self):
        self.bank_account_repository.bank_account = self.bank_account
        with self.assertRaises(BankAccountAlreadyExists):
            self.bank_account_services.create_bank_account(self.bank_account)

    def test_update_bank_account(self):
        self.bank_account_repository.bank_account = self.bank_account
        account = self.bank_account_services.update_by_id(self.bank_account.id)
        self.assertEqual(self.bank_account , account)

    def test_delete_bank_account(self):
        self.bank_account_repository.bank_account = self.bank_account
        account = self.bank_account_services.delete_by_id(self.bank_account.id)
        self.assertEqual(self.bank_account , account)

class BankAccountRepositorySpy:
    def __init__(self):
        self.bank_account = None

    def get_by_id(self , id):
        if self.bank_account and self.bank_account.id == id:
            return self.bank_account
        return None

    def get_by_user_id(self , user_id):
        if self.bank_account and self.bank_account.user_id == user_id:
            return self.bank_account
        return None
    def create(self, bank_account):
        self.bank_account = bank_account
        return self.bank_account

    def update_by_id(self , id):
        if self.bank_account and self.bank_account.id == id:
            return self.bank_account
        return None

    def delete_by_id(self , id):
        if self.bank_account and self.bank_account.id == id:
            return self.bank_account
        return None

class BankAccountDouble:
    def __init__(self ,
                 id = '123',
                 account_number ='123456789',
                 account_type= AccountType.SAVINGS,
                 balance=1000 ,
                 is_active=True,
                 user_id = '1'):
        self.id = id
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.is_active = is_active
        self.user_id = user_id

if __name__ == '__main__':
    unittest.main()