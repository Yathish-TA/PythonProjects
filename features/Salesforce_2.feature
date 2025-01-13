Feature: Creating New Account and adding the contact and opportunity

  Scenario Outline: Valid Login
    Given I am on the Salesforce login page
    When I enter valid credentials "<Username>" and "<Password>"
    Then I should see the Salesforce dashboard
    Examples:
      | Username                     | Password    |
      | yathish.gowda-c5kb@force.com | Yathish@123 |

  Scenario Outline: Create an New Account
    Given User is on Home Page
    When Click on Accounts dropdown and click New account
    And Enter "<Account_Name>"
    And Click on Save button of Account
    Then Verify the The Account is Created by the "<Account_Name>"
    Examples:
      | Account_Name |
      | AXIS         |

  Scenario Outline: Add Contact and Opportunity to the Account created
    Given User is on Account Page
    When Click on New Contact Link
    And Enter contact "<Last_Name>"
    And Click on Save button of Contact or Opportunity window
    Then Verify the The contact is added with "<Last_Name>"
    When Click on New Opportunity Link
    And Enter Opportunity "<Opp_Name>"
    And Click on Save button of Contact or Opportunity window
    Then Verify the The Opportunity is added with "<Opp_Name>"
    Examples:
      | Last_Name | Opp_Name      |
      | Gopal     | AXIS BANK OPP |
