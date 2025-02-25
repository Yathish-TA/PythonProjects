import time
from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.ACCOUNT_DROPDOWN = (By.XPATH, "//a[@title='Leads']/following::a[@role='button'][3]")
        self.NEW_ACCOUNT = (By.XPATH, "//span[text()='New Account']")
        self.ACCOUNT_NAME = (By.XPATH, "//input[@name='Name']")
        self.ACCOUNT_SAVE = (By.XPATH, "//button[@name='SaveEdit']")
        self.ACCOUNT_FINAL_NAME = (By.XPATH, "(//slot[@name='primaryField']/lightning-formatted-text)")
        self.NEW_CONTACT = (By.XPATH, "(//button[@name='Global.NewContact'])")
        self.CONTACT_LASTNAME = (By.XPATH, "//input[@placeholder='Last Name']")
        self.CONTACT_OPPORTUNITY_SAVE = (By.XPATH, "(//span[text()='Save'])[3]")
        self.NEW_OPPORTUNITY = (By.XPATH, "(//button[@name='Global.NewOpportunity'])")
        self.OPPORTUNITY_NAME = (By.XPATH, "(//input[@class=' input'])[1]")
        self.CREATED_CONTACT_NAME = (By.XPATH, "//*[@aria-label='Contacts']//span[@class='slds-truncate']/slot")
        self.CREATED_OPPORTUNITY_NAME = (By.XPATH, "//*[@aria-label='Opportunities']//span[@class='slds-truncate']/slot")
        self.ACCOUNT_SEARCH_BAR = (By.XPATH, "//input[@name='Account-search-input']")
        self.SELECT_SEARCHED_ACCOUNT = (By.XPATH, "(//table[@aria-label='All Accounts']//span/a)[1]")
        self.CONTACT_NAME = (By.XPATH, "(//a[@id='window']/span)[1]")
        self.OPP_NAME = (By.XPATH, "(//a[@id='window']/span)[2]")



    def clickAccountDropDown(self):
        time.sleep(2)
        self.driver.find_element(*self.ACCOUNT_DROPDOWN).click()

    def clickNewAccount(self):
        element = self.driver.find_element(*self.NEW_ACCOUNT)
        self.driver.execute_script("arguments[0].click();", element)

    def enterAccountName(self, acc_name):
        self.driver.find_element(*self.ACCOUNT_NAME).send_keys(acc_name)

    def clickSaveAccount(self):
        self.driver.find_element(*self.ACCOUNT_SAVE).click()
        time.sleep(2)

    def verifyCreatedAccountName(self):
        self.driver.refresh()
        time.sleep(2)
        return self.driver.find_element(*self.ACCOUNT_FINAL_NAME).text
