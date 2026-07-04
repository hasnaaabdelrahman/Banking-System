from behave import given, when, then

@given("the user")
def step_impl(context):
    context.user = {
        "username" : "user_123",
        "password" : "password@12",
        "email" : "user@example.com",
        "first_name" : "fuser",
        "last_name" : "luser",
        "age" : 20,
        "image" : "https://example.com"
    }

@when("the user enters the valid values")
def step_impl(context):
    context.result = True

@then("the register should be successfully")
def step_impl(context):
    assert context.result is True

@given("the user is trying to register")
def step_impl(context):
    context.user = {
        "username": "",
        "password": "password@12",
        "email": "",
        "first_name": "fuser",
        "last_name": "luser",
        "age": 20,
        "image": "https://example.com"
    }
@when("the users enters the invalid values")
def step_impl(context):
    context.result = False

@then("the register should not be happened")
def step_impl(context):
    assert context.result is False
