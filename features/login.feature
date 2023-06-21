#Feature: Check the functionality of the login page
#
#  @correct_credentials
#  Scenario: Check that you can login into the application when providing correct credentials
#    Given I am on the jules login page
#    When I insert email "stoican.adrian@yahoo.com" and password "P12345p!"
#    And I click login button
#    Then I can login into the jules app
#    Then I can logout
##
#  @invalid_credentials
#  Scenario Outline: Check that you cannot login into the application when providing invalid credentials
#    Given I am on the jules login page
#    When I insert email "<email>" and password "<password>"
#    And I click login button
#    Then I cannot login into the jules app and I receive error
#
#     Examples:
#    | email | password |
#    | stoican.adrian@yahoo.com | P12345p!11 |
#    | incorect_email@yahoo.com | P12345p!|
#
#  Scenario: Check that you cannot login into the application when providing correct email and delete password
#    Given I am on the jules login page
#    When I insert email "stoican.adrian@yahoo.com" and delete password
#    Then I cannot login into the jules app because no password was introduced
