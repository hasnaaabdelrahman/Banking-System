from models.bank_account import BankAccount
from exceptions.bank_account_exceptions import BankAccountNotFound , BankAccountAlreadyExists
from schemas.bank_account_schema import BankAccountSchema


class BankAccountService:
    def __init__(self , bank_repository):
        self.bank_repository = bank_repository

    def create_bank_account(self , bank_account_data:BankAccountSchema) -> BankAccount:
        account = self.bank_repository.get_by_user_id (bank_account_data.user_id)
        if account:
            raise BankAccountAlreadyExists("Bank account already exists")
        bank_account =BankAccount(
            account_type= bank_account_data.account_type,
            is_active= bank_account_data.is_active,
            balance= bank_account_data.balance,
            user_id=bank_account_data.user_id
        )
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
        return self.bank_repository.delete(id)

    def update_by_id(self , id:str) -> BankAccount|None:
        account = self.bank_repository.get_by_id(id)
        if not account:
            raise BankAccountNotFound("Bank account not found")
        return self.bank_repository.update(account)