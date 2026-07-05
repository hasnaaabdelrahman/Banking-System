Feature: Transaction Creation

  Scenario: Transaction is created successfully
    Given the user wants to create a transaction
    When the user is registered and logged in and the user is already has an bank account
    Then the transaction is created successfully
