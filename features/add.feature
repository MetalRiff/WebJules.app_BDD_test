Feature: Check the base functionality of the add page

    Scenario: Check that you can add item
      Given I am on the jules login page
      When I insert email "stoican.adrian@yahoo.com" and password "P12345p!"
      And I click login button
      And I click on Add button
      Then I can add Airplane A380 item to one of my records
      Then I can logout