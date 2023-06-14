Feature: Check the functionality of the login page


  Scenario: Check that you can login into the application when providing correct credentials
    Given I am on the jules login page
    When I insert correct email and correct password
    And I click login button
    Then I can login into the jules app
    Then I can logout

  Scenario: Check that you cannot login into the application when providing correct email and incorrect password
    Given I am on the jules login page
    When I insert correct email and incorrect password
    And I click login button
    Then I cannot login into the jules app

  Scenario: Check that you cannot login into the application when providing incorrect email and correct password
    Given I am on the jules login page
    When I insert incorrect email and correct password
    Then I cannot login into the jules app because no valid email was introduced

  Scenario: Check that you cannot login into the application when providing correct email and delete password
    Given I am on the jules login page
    When I insert correct email and delete password
    Then I cannot login into the jules app because no password was introduced