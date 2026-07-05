Feature: Create Bank Account

  Scenario:  Bank Account is Created Successfully
      Given the user wants to create a bank account
      When  the user is registered and logged in
      Then  the bank account is created successfully

  Scenario: Bank Account is not created
    Given the user is registered and logged in and wants to create a bank account
    When the user is already has an bank account
    Then the bank account is not created

