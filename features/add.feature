Feature: Check the base functionality of the add page


  Scenario: Check that you can access Add page
      Given I am on the jules login page
      When I insert email "stoican.adrian@yahoo.com" and password "P12345p!"
      And I click login button
      Then I can click on Add button
      Then I can click the Close button
      Then I can logout

    Scenario: Check that you can add multiple items
      Given I am on the jules login page
      When I insert email "stoican.adrian@yahoo.com" and password "P12345p!"
      And I click login button
      Then I can add Airbus airplane items to my records
      Then I can logout