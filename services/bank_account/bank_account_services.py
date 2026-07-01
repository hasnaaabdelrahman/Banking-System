from models.bank_account import BankAccount
from exceptions.bank_account_exceptions import BankAccountNotFound , BankAccountAlreadyExists


class BankAccountService:
    def __init__(self , bank_repository):
        self.bank_repository = bank_repository

    def create_bank_account(self , bank_account:BankAccount) -> BankAccount:
        if self.bank_repository.get_by_id(bank_account.id) or self.bank_repository.get_by_user_id(bank_account.user_id):
            raise BankAccountAlreadyExists("Bank account already exists")
        self.bank_repository.create(bank_account)
        return bank_account

    def get_by_id(self , id:str) -> BankAccount:
        account = self.bank_repository.get_by_id(id)
        if account is None:
            raise BankAccountNotFound("Bank account not found")
        return self.bank_repository.get_by_id(id)

    def get_by_user_id(self , user_id:str) -> BankAccount:
        account = self.bank_repository.get_by_user_id(user_id)
        if account is None:
            raise BankAccountNotFound("Bank account not found")
        return self.bank_repository.get_by_user_id(user_id)

    def delete_by_id(self , id:str) -> bool:
        account = self.bank_repository.get_by_id(id)
        if account is None:
            raise BankAccountNotFound("Bank account not found")
        return self.bank_repository.delete_by_id(id)

    def update_by_id(self , id:str) -> bool:
        account = self.bank_repository.get_by_id(id)
        if account is None:
            raise BankAccountNotFound("Bank account not found")
        return self.bank_repository.update_by_id(id)