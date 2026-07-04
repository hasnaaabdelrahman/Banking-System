Feature: User Login

    Scenario: Successful Login
        Given the user is registered
        When the user enters the valid credentials
        Then the login should be successfully