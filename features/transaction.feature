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

  Scenario: Get Transaction by id successfully
    Given trying to get a transaction by id
    When transaction exists with this id
    Then the transaction should be found successfully

  Scenario: Cannot get transaction by id
    Given trying to get a transaction with id
    When transaction not exists with this id
    Then the transaction should not be found

  Scenario: Get Transaction by account id successfully
    Given trying to get a transaction by account id
    When transaction exists with this account id
    Then the transaction found successfully

  Scenario: Cannot get transaction by account id
    Given trying to get a transaction with account id
    When transaction not exists with this account id
    Then the transaction should not be exists

  Scenario: Update Transaction Successfully
    Given the user wants to update specific transaction
    When the transaction is already exists
    Then the transaction should be updated successfully

  Scenario: Cannot Update Transaction
    Given the user is trying to update specific transaction
    When the transaction is not exists
    Then the transaction should not be updated

  Scenario: delete Transaction Successfully
    Given the user wants to delete specific transaction
    When the transaction is exists
    Then the transaction should be deleted successfully
