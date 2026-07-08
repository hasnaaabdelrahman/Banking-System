Feature: Create Bank Account

  Scenario:  Bank Account is Created Successfully
    Given the user wants to create a bank account
    When  the user is registered and logged in
    Then  the bank account is created successfully

  Scenario: Bank Account is not created
    Given the user is registered and logged in and wants to create a bank account
    When the user is already has an bank account
    Then the bank account is not created

  Scenario: Get The Bank Account by id Successfully
    Given trying to get a bank account by id
    When the bank account already exists
    Then the bank account should be found

  Scenario: Cannot Get The Bank Account by id
    Given trying to get a bank account with id
    When the bank account is not found
    Then the bank account not be found

  Scenario: Get The Bank Account by user id
    Given trying to get a bank account by user id
    When the bank account already exists with user id
    Then the bank account is found successfully

  Scenario: Can not get The Bank Account by user id
    Given trying to get a bank account with user id
    When the bank account not exists with user id
    Then the bank account not found

  Scenario: Update the bank account successfully
    Given the user wants to update his bank account
    When the bank account is exists
    Then the bank account should be updated successfully

  Scenario: Cannot Update the bank account
    Given the user is trying to update his bank account
    When the bank account is not exists
    Then the bank account should not be updated

  Scenario: Delete the bank account successfully
    Given the user wants to delete his bank account
    When the bank account is found
    Then the bank account should be deleted successfully

  Scenario:Cannot delete the bank account
    Given the user is trying to delete his bank account
    When the bank account not found
    Then the bank account should not be deleted