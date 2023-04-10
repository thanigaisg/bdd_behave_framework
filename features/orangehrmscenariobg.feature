Feature: orangehrm login

  Background: common steps
    Given launch chrome browser
    When open orangehrm homepage
    And then enter valid username and password
    And click on login button

  @mustrun @e2erun
  Scenario: login to orangehrm with valid parameters
    Then user must login into the dashboard page

  @optionalrun @e2erun
  Scenario: search user
    When navigate to search page
    Then search page should display
