from pytest_bdd import scenarios, given, when, then, parsers
# Adding dummy comment line

# Load the feature file
scenarios("../features/UseCase2.feature")


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


@given(u'Click on Contact dropdown and click New contact')
def step_impl(contact_page):
    contact_page.clickContactDropDown()
    contact_page.clickNewContact()


@when(parsers.parse(u'Enter "{LastName}" and Select the "{Account_Name}" created recently'))
def step_impl(contact_page, LastName, Account_Name):
    contact_page.enterContactLastName(LastName)
    contact_page.enterContactAccountName(Account_Name)
    contact_page.selectContactAccName()


@when(u'Click on Save button of Contact')
def step_impl(contact_page):
    contact_page.clickSaveContact()


@then(parsers.parse(u'Verify the The Contact is Created by the "{LastName}"'))
def step_impl(contact_page, LastName):
    assert contact_page.verifyCreatedContactName() == LastName


@given(u'Click on Opportunity dropdown and click New Opportunity')
def step_impl(opp_page):
    opp_page.clickOppDropDown()
    opp_page.clickNewOpp()


@when(u'select stage')
def step_impl(opp_page):
    opp_page.selectOppStage("Propose")


@given(parsers.parse(u'Click on Opportunity dropdown and click New Opportunity'))
def step_impl(opp_page):
    opp_page.clickOppDropDown()
    opp_page.clickNewOpp()


@when(parsers.parse(u'Enter "{OppName}" and Select the "{AccountName}" created previously'))
def step_impl(opp_page, OppName, AccountName):
    opp_page.enterOppName(OppName)
    opp_page.enterOppAccountName(AccountName)
    opp_page.selectOppAccountName()


@when(parsers.parse(u'Enter the opportunity close date as "{CloseDate}"'))
def step_impl(opp_page, CloseDate):
    opp_page.enterCloseDate(CloseDate)


@when(parsers.parse(u'Select opportunity stage as "{Opp_stage}"'))
def step_impl(opp_page, Opp_stage):
    opp_page.selectOppStage(Opp_stage)


@when(parsers.parse(u'Select opportunity forecast as "{Opp_forecast}"'))
def step_impl(opp_page, Opp_forecast):
    opp_page.selectOppForecast(Opp_forecast)


@when(parsers.parse(u'Click on Save button of Contact'))
def step_impl(opp_page):
    opp_page.clickSaveOpp()


@then(parsers.parse(u'Verify the The Opportunity is Created by the "{OppName}"'))
def step_impl(opp_page, OppName):
    assert opp_page.verifyCreatedOppName() == OppName
