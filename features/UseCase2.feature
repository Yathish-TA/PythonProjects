Feature: Salesforce Login
  As a user, I want to login and create an account and need to attach contact and opportunity to the created account.

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
      | WWW          |


  Scenario Outline: Create New Contact and attach to the above created account
    Given Click on Contact dropdown and click New contact
    When Enter "<LastName>" and Select the "<Account_Name>" created recently
    And Click on Save button of Contact
    Then Verify the The Contact is Created by the "<LastName>"
    Examples:
      | LastName | Account_Name |
      | CCC      | WWW          |


  Scenario Outline: Create New Opportunity and attach to the above created account
    Given Click on Opportunity dropdown and click New Opportunity
    When Enter "<OppName>" and Select the "<AccountName>" created previously
    And Enter the opportunity close date as "<CloseDate>"
    And Select opportunity stage as "<Opp_stage>"
    And Select opportunity forecast as "<Opp_forecast>"
    And Click on Save button of Contact
    Then Verify the The Opportunity is Created by the "<OppName>"
    Examples:
      | OppName | AccountName | CloseDate  | Opp_stage | Opp_forecast |
      | OppNam2 | WWW         | 13/03/2025 | Propose   | Commit       |
