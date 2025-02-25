import logging
# Adding dummy comment line

from pytest_bdd import scenarios, given, when, then, parsers

# Load the feature file
scenarios("../features/UseCase1.feature")


# Step Definitions
@given("I open the Salesforce login page")
def open_login_page(login_page):
    login_page.open_login_page("https://login.salesforce.com")


@when(parsers.parse(u'I enter username "{username}" and password "{password}"'))
def enter_credentials(login_page, username, password):
    login_page.enter_username(username)
    login_page.enter_password(password)


@when("I click the login button")
def click_login(login_page):
    login_page.click_login()


@then("I should see the Salesforce dashboard")
def verify_dashboard(login_page):
    assert login_page.is_dashboard_displayed()


@given("User is on Home Page")
def home_page(lead_page):
    pass


@when("Click on Leads dropdown and click New Lead link")
def clicNewLead(lead_page):
    lead_page.clickLeadsDropDown()
    lead_page.clickNewLead()


@when(parsers.parse('Enter "{LastName}" and "{Company}"'))
def fillDetails(lead_page, LastName, Company):
    lead_page.enterTheDetails(LastName, Company)


@when('Click on Save button')
def SaveLead(lead_page):
    lead_page.clickSaveLead()


@then(parsers.parse('Verify the The Lead is Created by the "{LastName}"'))
def VerifyLead(lead_page, LastName):
    assert lead_page.verifyCreatedLeadName() == LastName
    logging.info("Verified the Lead creation Successfully")


@when(u'User clicks on convert link')
def leadConvert(lead_page):
    lead_page.clickLeadConvert()


@when(parsers.parse('User goes with this type of Account "{AccType}" and AccName "{AccName}"'))
def convertingLead(lead_page, AccType, AccName):
    lead_page.newOrExistingAccount(AccType, AccName)


@when(u'User clicks on Convert Button on Convert tab')
def convertButton(lead_page):
    lead_page.clickConvertButton()


@then(parsers.parse(u'Verify Converted "{Message}" is displayed'))
def verifyConvertion(lead_page, Message):
    assert lead_page.verifyConvertedOrNot() == Message


@then(u'Close the Lead Popup screen')
def step_impl(lead_page):
    lead_page.closeLeadPopup()


@when(u'Click on Accounts dropdown and click New account')
def step_impl(account_page):
    account_page.clickAccountDropDown()
    account_page.clickNewAccount()


@when(parsers.parse(u'Enter "{AccountName}"'))
def step_impl(account_page, AccountName):
    account_page.enterAccountName(AccountName)


@when(u'Click on Save button of Account')
def step_impl(account_page):
    account_page.clickSaveAccount()


@then(parsers.parse(u'Verify the The Account is Created by the "{AccountName}"'))
def step_impl(account_page, AccountName):
    assert account_page.verifyCreatedAccountName() == AccountName

