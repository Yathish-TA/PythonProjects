import logging

from behave import given, when, then

from pages.account_page import AccountPage
from pages.lead_page import LeadPage
from pages.login_page import LoginPage


@given(u'I am on the Salesforce login page')
def open_login_page(context):
    context.login_page = LoginPage(context.browser)
    context.login_page.open()


@when(u'I enter valid credentials "{username}" and "{password}"')
def enter_credentials(context, username, password):
    print(username + password)
    context.login_page.login(username, password)


@then(u'I should see the Salesforce dashboard')
def verify_dashboard(context):
    assert context.login_page.is_dashboard_displayed()


@given(u'User is on Home Page')
def home_page(context):
    context.login_page = LoginPage(context.browser)
    assert context.login_page.is_dashboard_displayed()


@when(u'Click on Leads dropdown and click New Lead')
def clicNewLead(context):
    context.lead_page = LeadPage(context.browser)
    context.lead_page.clickLeadsDropDown()
    context.lead_page.clickNewLead()


@when(u'Enter "{LastName}" and "{Company}"')
def fillDetails(context, LastName, Company):
    context.lead_page.enterTheDetails(LastName, Company)


@when(u'Click on Save button')
def SaveLead(context):
    context.lead_page.clickSaveLead()


@then(u'Verify the The Lead is Created by the "{LastName}"')
def VerifyLead(context,LastName):
    assert context.lead_page.verifyCreatedLeadName() == LastName
    logging.info("Verified the Lead creation Successfully")


@given(u'User is on Lead Page')
def userLeadPage(context):
    context.lead_page = LeadPage(context.browser)
    assert context.lead_page.isUserOnLeadPage()


@when(u'User clicks on convert link')
def leadConvert(context):
    context.lead_page.clickLeadConvert()


@when(u'User clicks on Convert Button on Convert tab')
def convertButton(context):
    context.lead_page.clickConvertButton()


@then(u'Verify Converted "{Message}" is displayed')
def verifyConvertion(context,Message):
    assert context.lead_page.verifyConvertedOrNot() == Message


@when(u'Click on Accounts dropdown and click New account')
def step_impl(context):
    context.account_page = AccountPage(context.browser)
    context.account_page.clickAccountDropDown()
    context.account_page.clickNewAccount()


@when(u'Enter "{AccountName}"')
def step_impl(context, AccountName):
    context.account_page.enterAccountName(AccountName)


@when(u'Click on Save button of Account')
def step_impl(context):
    context.account_page.clickSaveAccount()


@then(u'Verify the The Account is Created by the "{AccountName}"')
def step_impl(context, AccountName):
    assert context.account_page.verifyCreatedAccountName() == AccountName


@given(u'User is on Account Page')
def step_impl(context):
    context.account_page = AccountPage(context.browser)
    assert context.account_page.isUserOnAccountPage()


@when(u'Click on New Contact Link')
def step_impl(context):
    context.account_page.clickNewContact()


@when(u'Enter contact "{LastName}"')
def step_impl(context,LastName):
    context.account_page.enterContactDetails(LastName)


@when(u'Click on Save button of Contact or Opportunity window')
def step_impl(context):
    context.account_page.clickSaveAccOrOpp()


@then(u'Verify the The contact is added with "{LastName}"')
def step_impl(context, LastName):
    assert context.account_page.verifyContactAdded() == LastName


@when(u'Click on New Opportunity Link')
def step_impl(context):
    context.account_page.clickNewOpportunity()


@when(u'Enter Opportunity "{Opp_Name}"')
def step_impl(context,Opp_Name):
    context.account_page.enterOpportunityName(Opp_Name)


@then(u'Verify the The Opportunity is added with "{Opp_Name}"')
def step_impl(context,Opp_Name):
    assert context.account_page.verifyOpportunityAdded() == Opp_Name
