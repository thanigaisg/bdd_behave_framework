Feature: orangehrm logo
  Scenario: logo presence on orangehrm home page
    Given launch chrome browser
    When  open orangehrm homepage
    Then  verify that logo present on that home page
    And   close browser