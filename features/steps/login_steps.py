from behave import given, when, then

from exceptions.user_exceptions import InvalidCredentials, UserNotFound
from models.user import User
from schemas.user_schema import UserLoginSchema
from utils import password

@given("the user is registered")
def step_impl(context):
    context.user = User(
        username="user_123",
        password="password@12",
        email="user1@example.com",
        first_name="fuser",
        last_name="luser",
        age=20,
        img_url="https://example.com",
        bank_account=[]
    )
    context.user =  context.user_service.register(context.user)

@when("the user enters the valid credentials")
def step_impl(context):
    user_data = UserLoginSchema(
        username="user_123",
        password="password@12",
    )
    context.result = context.user_service.login(user_data)

@then("the login should be successfully")
def step_impl(context):
    assert context.result is not None
    assert context.result.username == "user_123"


@given("the user is trying to login")
def step_impl(context):
    context.user = context.user = UserLoginSchema(
        username = "user_123",
        password = "password123"
    )
@when("the user enters the invalid credentials")
def step_impl(context):
    try:
        context.result = context.user_service.login(context.user)
    except (UserNotFound, InvalidCredentials) as e:
        context.exception = e

@then("the login should not be successfully")
def step_impl(context):
    assert isinstance(context.exception, UserNotFound)