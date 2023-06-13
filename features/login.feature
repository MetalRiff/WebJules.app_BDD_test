Feature: Check the functionality of the login page


# Scenariul 1: username corect + parola corecta
# Scenariul 2: username corect + parola incorecta
# Scenariul 3: username incorect + parola corecta
# Scenariul 4: username incorect + parola incorecta
# Scenariul 5: username None + parola corecta
# Scenariul 6: username None + parola incorecta
# Scenariul 7: username corect + parola None
# Scenariul 8: username incorect + parola None
# Scenariul 9: username None + parola None

  Scenario: Check that you can login into the application when providing correct credentials
    Given I am on the jules login page
    When I insert correct user name and correct password
    And I click login button
    Then I can login into the jules app