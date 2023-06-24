Feature: Check the base functionality of the search page

  Scenario: Check that you can select Record filter after login into the application when providing correct credentials
    Given I am on the jules login page
    When I insert email "stoican.adrian@yahoo.com" and password "P12345p!"
    And I click login button
    Then I can select Record filter
    Then I can logout


  Scenario: Check that you can select Type filter after login into the application when providing correct credentials
    Given I am on the jules login page
    When I insert email "stoican.adrian@yahoo.com" and password "P12345p!"
    And I click login button
    Then I can select Type filter
    Then I can logout


  Scenario: Check that you can select Category filter after login into the application when providing correct credentials
    Given I am on the jules login page
    When I insert email "stoican.adrian@yahoo.com" and password "P12345p!"
    And I click login button
    Then I can select Category filter
    Then I can logout

  Scenario: Check that you can select Tag filter after login into the application when providing correct credentials
    Given I am on the jules login page
    When I insert email "stoican.adrian@yahoo.com" and password "P12345p!"
    And I click login button
    Then I can select Tag filter
    Then I can logout


  Scenario: Check that you can select Connection filter after login into the application when providing correct credentials
    Given I am on the jules login page
    When I insert email "stoican.adrian@yahoo.com" and password "P12345p!"
    And I click login button
    Then I can select Connection filter
    Then I can logout

  @delete_item
  Scenario: Delete recorded item
    Given I am on the jules login page
    When I insert email "stoican.adrian@yahoo.com" and password "P12345p!"
    And I click login button
    Then I can delete A380 airplane
    Then I can logout