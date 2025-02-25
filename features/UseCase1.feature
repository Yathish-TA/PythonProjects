Feature: Salesforce Login
  As a user, I want to log in to the Salesforce application with valid credentials.


  Scenario Outline: Successful login with valid credentials
    Given I open the Salesforce login page
    When I enter username "<username>" and password "<password>"
    And I click the login button
    Then I should see the Salesforce dashboard

    Examples:
      | username                     | password    |
      | yathish.gowda-c5kb@force.com | Yathish@123 |


  Scenario Outline: Create an New Account
    Given User is on Home Page
    When Click on Accounts dropdown and click New account
    And Enter "<Account_Name>"
    And Click on Save button of Account
    Then Verify the The Account is Created by the "<Account_Name>"
    Examples:
      | Account_Name |
      | LIC           |

  Scenario Outline: Create a Lead and convert the Lead with new and existing account
    Given User is on Home Page
    When Click on Leads dropdown and click New Lead link
    And Enter "<LastName>" and "<Company>"
    And Click on Save button
    Then Verify the The Lead is Created by the "<LastName>"
    When User clicks on convert link
    And User goes with this type of Account "<AccType>" and AccName "<AccName>"
    And User clicks on Convert Button on Convert tab
    Then Verify Converted "<Message>" is displayed
    And Close the Lead Popup screen
    Examples:
      | LastName | Company | AccType  | AccName | Message                      |
      | Mango    | Fruits  | Existing | LIC     | Your lead has been converted |
      | Carrot   | Veg     | New      | -       | Your lead has been converted |

