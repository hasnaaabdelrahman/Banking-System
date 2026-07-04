Feature: User Login

    Scenario: Successful Login
        Given the user is registered
        When the user enters the valid credentials
        Then the login should be successfully

    Scenario: Failure Login
        Given the user is trying to login
        When the user enters the invalid credentials
        Then the login should not be successfully