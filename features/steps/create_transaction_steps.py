from models import User
from models.bank_account import BankAccount
from models.transaction import Transaction
from behave import given, when, then
from datetime import datetime
from common.transaction_type import TransactionType
from common.account_type import AccountType


@given("the user wants to create a transaction")
def step_impl(context):
    context.transaction = Transaction(
        id='1',
        account_id='123',
        transaction_type=TransactionType.DEPOSIT,
        amount=1000,
        date=datetime.now()
    )
@when("the user is registered and logged in and the user is already has an bank account")
def step_impl(context):
    context.bank_account = BankAccount(
        id='123',
        account_number='123456789',
        account_type=AccountType.SAVINGS,
        balance=1000,
        is_active=True,
        user_id='1'
    )
    context.user = User(
        id = '1',
        username="user_13",
        password="password@12",
        email="user1@example.com",
        first_name="fuser",
        last_name="luser",
        age=20,
        img_url="https://example.com",
        bank_account=[]
    )
    context.user = context.user_service.register(context.user)
    context.logged = context.user_service.login("user_13", "password@12")
    context.bank = context.bank_account_service.create_bank_account(context.bank_account)
    context.transaction = context.transaction_service.create_transaction(context.transaction)

@then("the transaction is created successfully")
def step_impl(context):
    assert context.transaction is not None