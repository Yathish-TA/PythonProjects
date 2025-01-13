import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccountPage(BasePage):

    ACCOUNT_DROPDOWN = (By.XPATH, "//a[@title='Leads']/following::a[@role='button'][3]")
    NEW_ACCOUNT = (By.XPATH, "//span[text()='New Account']")
    ACCOUNT_NAME = (By.XPATH, "//input[@name='Name']")
    ACCOUNT_SAVE = (By.XPATH,"//button[@name='SaveEdit']")
    ACCOUNT_FINAL_NAME = (By.XPATH,"(//slot[@name='primaryField']/lightning-formatted-text)")
    NEW_CONTACT = (By.XPATH,"(//button[@name='Global.NewContact'])")
    CONTACT_LASTNAME = (By.XPATH,"//input[@placeholder='Last Name']")
    CONTACT_OPPORTUNITY_SAVE = (By.XPATH,"(//span[text()='Save'])[3]")
    NEW_OPPORTUNITY = (By.XPATH,"(//button[@name='Global.NewOpportunity'])")
    OPPORTUNITY_NAME = (By.XPATH,"(//input[@class=' input'])[1]")
    CREATED_CONTACT_NAME = (By.XPATH,"//*[@aria-label='Contacts']//span[@class='slds-truncate']/slot")
    CREATED_OPPORTUNITY_NAME = (By.XPATH,"//*[@aria-label='Opportunities']//span[@class='slds-truncate']/slot")



    def clickAccountDropDown(self):
        time.sleep(5)
        self.clickByLocator(self.ACCOUNT_DROPDOWN)

    def clickNewAccount(self):
        self.clickUsingAction(self.NEW_ACCOUNT)

    def enterAccountName(self,acc_name):
        self.wait_for_element(self.ACCOUNT_NAME).send_keys(acc_name)

    def clickSaveAccount(self):
        self.clickByLocator(self.ACCOUNT_SAVE)


    def verifyCreatedAccountName(self):
        return self.wait_for_element(self.ACCOUNT_FINAL_NAME).text

    def clickNewContact(self):
        self.clickByLocator(self.NEW_CONTACT)

    def enterContactDetails(self,Contact_LN):
        self.wait_for_element(self.CONTACT_LASTNAME).send_keys(Contact_LN)

    def clickSaveAccOrOpp(self):
        self.clickByLocator(self.CONTACT_OPPORTUNITY_SAVE)

    def verifyContactAdded(self):
        return self.wait_for_element(self.CREATED_CONTACT_NAME).text

    def clickNewOpportunity(self):
        self.clickByLocator(self.NEW_OPPORTUNITY)

    def enterOpportunityName(self, Opp_Name):
        self.wait_for_element(self.OPPORTUNITY_NAME).clear()
        self.wait_for_element(self.OPPORTUNITY_NAME).send_keys(Opp_Name)

    def verifyOpportunityAdded(self):
        return self.wait_for_element(self.CREATED_OPPORTUNITY_NAME).text

    def isUserOnAccountPage(self):
       return self.wait_for_element(self.ACCOUNT_FINAL_NAME)