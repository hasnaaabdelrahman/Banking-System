Feature: Transaction Creation

  Scenario: Transaction is created successfully
    Given the user wants to create a transaction
    When the user is registered and logged in and the user is already has an bank account
    Then the transaction is created successfully

  Scenario: Transaction cannot be created with an invalid amount
      Given the user is registered
      And the user is logged in
      And the user has a bank account
      When the user attempts to create a transaction with an invalid amount
      Then the transaction should not be created
