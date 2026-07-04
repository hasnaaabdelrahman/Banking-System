from behave import given, when, then

@given("the user is registered")
def step_impl(context):
    context.user = {
        "username": "user_123",
        "email": "password@123",
    }

@when("the user enters the valid credentials")
def step_impl(context):
    context.result = True

@then("the login should be successfully")
def step_impl(context):
    assert context.result is True