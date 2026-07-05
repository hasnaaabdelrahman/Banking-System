
from behave import given, when, then

from common.account_type import AccountType
from exceptions.bank_account_exceptions import BankAccountAlreadyExists, BankAccountNotFound
from models import User
from models.bank_account import BankAccount

@given("the user wants to create a bank account")
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
@when("the user is registered and logged in")
def step_impl(context):
    context.user = context.user_service.register(context.user)
    context.logged = context.user_service.login("user_13", "password@12")
    context.result = context.bank_account_service.create_bank_account(context.bank_account)

@then("the bank account is created successfully")
def step_impl(context):
    assert context.result is not None

@given("the user is registered and logged in and wants to create a bank account")
def step_impl(context):
    context.bank_account = BankAccount(
        id='123',
        account_number='123456789',
        account_type=AccountType.SAVINGS,
        balance=1000,
        is_active=True,
        user_id='2'
    )
    context.user = User(
        username="user_23",
        password="password@12",
        email="user2@example.com",
        first_name="fuser",
        last_name="luser",
        age=22,
        img_url="https://example.com",
        bank_account=[]
    )
    context.user = context.user_service.register(context.user)
    context.logged = context.user_service.login("user_23", "password@12")
    context.result = context.bank_account_service.create_bank_account(context.bank_account)

@when("the user is already has an bank account")
def step_impl(context):
    try:
        context.result = context.bank_account_service.create_bank_account(context.bank_account)
    except (BankAccountAlreadyExists) as e:
        context.exception = e

@then("the bank account is not created")
def step_impl(context):
    assert isinstance(context.exception, BankAccountAlreadyExists)

@given("trying to get a bank account by id")
def step_impl(context):
    context.bank_account = BankAccount(
        id='123',
        account_number='123456789',
        account_type=AccountType.SAVINGS,
        balance=1000,
        is_active=True,
        user_id='1'
    )
    context.bank_account_service.create_bank_account(context.bank_account)

@when("the bank account already exists")
def step_impl(context):
    context.bank_account = context.bank_account_service.get_by_id(context.bank_account.id)

@then("the bank account should be found")
def step_impl(context):
    assert context.bank_account is not None

@given("trying to get a bank account with id")
def step_impl(context):
    context.bank_account = BankAccount(
        id='0',
        account_number='123456789',
        account_type=AccountType.SAVINGS,
        balance=1000,
        is_active=True,
        user_id='1'
    )
@when("the bank account is not found")
def step_impl(context):
    try:
        context.bank_account = context.bank_account_service.get_by_id(context.bank_account.id)
    except (BankAccountNotFound) as e:
        context.exception = e

@then("the bank account not be found")
def step_impl(context):
    assert isinstance(context.exception, BankAccountNotFound)

@given("trying to get a bank account by user id")
def step_impl(context):
    context.bank_account = BankAccount(
        id='123',
        account_number='123456789',
        account_type=AccountType.SAVINGS,
        balance=1000,
        is_active=True,
        user_id='1'
    )
    context.bank_account_service.create_bank_account(context.bank_account)

@when("the bank account already exists with user id")
def step_impl(context):
    context.bank_account = context.bank_account_service.get_by_user_id(context.bank_account.user_id)

@then("the bank account is found successfully")
def step_impl(context):
    assert context.bank_account is not None

@given("trying to get a bank account with user id")
def step_impl(context):
    context.bank_account = BankAccount(
        id='123',
        account_number='123456789',
        account_type=AccountType.SAVINGS,
        balance=1000,
        is_active=True,
        user_id='1'
    )

@when("the bank account not exists with user id")
def step_impl(context):
    try:
        context.bank_account = context.bank_account_service.get_by_user_id(context.bank_account.user_id)
    except (BankAccountNotFound) as e:
        context.exception = e

@then("the bank account not found")
def step_impl(context):
    assert isinstance(context.exception, BankAccountNotFound)