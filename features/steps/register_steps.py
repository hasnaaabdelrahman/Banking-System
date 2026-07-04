from behave import given, when, then
from models.user import User

@given("the user")
def step_impl(context):
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


@when("the user enters the valid values")
def step_impl(context):
    context.result = context.user_service.register(context.user)


@then("the register should be successfully")
def step_impl(context):
    assert context.result is not None
    assert context.result.username == "user_13"
    assert context.result.email == "user1@example.com"

@given("the user is trying to register")
def step_impl(context):
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
@when("the users enters the invalid values")
def step_impl(context):
    context.result = context.result = context.user_service.register(context.user)

@then("the register should not be happened")
def step_impl(context):
    assert context.result is not None
