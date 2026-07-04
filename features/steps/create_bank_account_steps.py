
from behave import given, when, then

from common.account_type import AccountType
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
    context.result = context.user_service.login("user_13", "password@12")


@then("the bank account is created successfully")
def step_impl(context):
    assert context.result is not None