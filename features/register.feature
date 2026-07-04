Feature: User Register

  Scenario: Successful Register
    Given the user
    When the user enters the valid values
    Then the register should be successfully