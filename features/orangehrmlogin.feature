Feature: orangehrm login

  Scenario: login to orangehrm with valid parameters
    Given launch chrome browser
    When open orangehrm homepage
    And then enter username Admin and password admin123
    And click on login button
    Then user must login into the dashboard page

  Scenario Outline: login to orangehrm with multiple parameters
    Given launch chrome browser
    When open orangehrm homepage
    And then enter username <username> and password <password>
    And click on login button
    Then user must login into the dashboard page

    Examples:
      | username | password |
      | Admin    | admin123 |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |
