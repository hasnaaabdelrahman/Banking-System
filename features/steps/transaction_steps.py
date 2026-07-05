from exceptions.transaction_exceptions import TransactionNotFound
from models import User, transaction
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


@given(" the user is registered")
def step_impl(context):
    context.user = User(
        id='1',
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

@given("the user is logged in")
def step_impl(context):
    context.logged = context.user_service.login(context.user.username, "password@12")

@given("the user has a bank account")
def step_impl(context):
    context.bank_account = BankAccount(
        id='123',
        account_number='123456789',
        account_type=AccountType.SAVINGS,
        balance=1000,
        is_active=True,
        user_id='1'
    )
    context.bank = context.bank_account_service.create_bank_account(context.bank_account)

@when("the user attempts to create a transaction with an invalid amount")
def step_impl(context):
    context.transaction = Transaction(
        id='1',
        account_id='123',
        transaction_type=TransactionType.DEPOSIT,
        amount=-1,
        date=datetime.now()
    )
    try:
        context.transaction = context.transaction_service.create_transaction(context.transaction)
    except ValueError as e:
        context.exception = e

@then("the transaction should not be created")
def step_impl(context):
    assert isinstance(context.exception, ValueError)

@given("trying to get a transaction by id")
def step_impl(context):
    context.transaction = Transaction(
        id='1',
        account_id='123',
        transaction_type=TransactionType.DEPOSIT,
        amount=10000,
        date=datetime.now()
    )
    context.transaction_service.create_transaction(context.transaction)

@when("transaction exists with this id")
def step_impl(context):
    context.transaction = context.transaction_service.get_transaction_by_id(context.transaction.id)

@then("the transaction should be found successfully")
def step_impl(context):
    assert context.transaction is not None

@given("trying to get a transaction with id")
def step_impl(context):
    context.transaction = Transaction(
        id='1',
        account_id='123',
        transaction_type=TransactionType.DEPOSIT,
        amount=10000,
        date=datetime.now()
    )

@when("transaction not exists with this id")
def step_impl(context):
    try:
        context.transaction = context.transaction_service.get_transaction_by_id(context.transaction.id)
    except(TransactionNotFound) as e:
        context.exception = e

@then("the transaction should not be found")
def step_impl(context):
    assert isinstance(context.exception, TransactionNotFound)

@given("trying to get a transaction by account id")
def step_impl(context):
    context.transaction = Transaction(
        id='1',
        account_id='123',
        transaction_type=TransactionType.DEPOSIT,
        amount=10000,
        date=datetime.now()
    )
    context.transaction_service.create_transaction(context.transaction)

@when("transaction exists with this account id")
def step_impl(context):
    context.transaction = context.transaction_service.get_transaction_by_account_id(context.transaction.account_id)

@then("the transaction found successfully")
def step_impl(context):
    assert context.transaction is not None


@given("trying to get a transaction with account id")
def step_impl(context):
    context.transaction = Transaction(
        id='1',
        account_id='123',
        transaction_type=TransactionType.DEPOSIT,
        amount=10000,
        date=datetime.now()
    )

@when("transaction not exists with this account id")
def step_impl(context):
    try:
        context.transaction = context.transaction_service.get_transaction_by_account_id(context.transaction.account_id)
    except(TransactionNotFound) as e:
        context.exception = e

@then("the transaction should not be exists")
def step_impl(context):
    assert isinstance(context.exception, TransactionNotFound)

