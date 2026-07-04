Feature: User Register

  Scenario: Successful Register
    Given the user
    When the user enters the valid values
    Then the register should be successfully

  Scenario: Failure Register
    Given the user is trying to register
    When the users enters the invalid values
    Then the register should not be happened