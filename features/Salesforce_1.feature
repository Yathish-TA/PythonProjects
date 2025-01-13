Feature: Creating New Lead and Converting that to an account from Lead Page.

  Scenario Outline: Valid Login
    Given I am on the Salesforce login page
    When I enter valid credentials "<Username>" and "<Password>"
    Then I should see the Salesforce dashboard
    Examples:
      | Username                     | Password    |
      | yathish.gowda-c5kb@force.com | Yathish@123 |

  Scenario Outline: Create a Lead
    Given User is on Home Page
    When Click on Leads dropdown and click New Lead
    And Enter "<LastName>" and "<Company>"
    And Click on Save button
    Then Verify the The Lead is Created by the "<LastName>"
    Examples:
      | LastName | Company |
      | Darshan  | Cinema  |

  Scenario Outline: Convert a Lead after a Lead created
    Given User is on Lead Page
    When User clicks on convert link
    And User clicks on Convert Button on Convert tab
    Then Verify Converted "<Message>" is displayed
    Examples:
      | Message                      |
      | Your lead has been converted |

