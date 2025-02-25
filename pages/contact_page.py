import time
from selenium.webdriver.common.by import By


class ContactPage:

    def __init__(self, driver):
        self.driver = driver
        self.CONTACT_DROPDOWN = (By.XPATH, "//a[@title='Leads']/following::a[@role='button'][2]")
        self.NEW_CONTACT = (By.XPATH, "//span[text()='New Contact']")
        self.CONTACT_LAST_NAME = (By.XPATH, "//input[@name='lastName']")
        self.CONTACT_ACCOUNT_SEARCH = (By.XPATH, "//input[@placeholder='Search Accounts...']")
        self.CONTACT_1ST_ACC_SEARCH = (By.XPATH, "//li[@class='slds-listbox__item'][1]")
        self.CONTACT_SAVE = (By.XPATH, "//button[@name='SaveEdit']")
        self.CONTACT_FINAL_NAME = (By.XPATH, "//slot[@name='primaryField']/lightning-formatted-name")

    def clickContactDropDown(self):
        time.sleep(2)
        self.driver.find_element(*self.CONTACT_DROPDOWN).click()

    def clickNewContact(self):
        element = self.driver.find_element(*self.NEW_CONTACT)
        self.driver.execute_script("arguments[0].click();", element)

    def enterContactLastName(self, last_name):
        self.driver.find_element(*self.CONTACT_LAST_NAME).send_keys(last_name)

    def enterContactAccountName(self, acc_name):
        self.driver.find_element(*self.CONTACT_ACCOUNT_SEARCH).clear()
        self.driver.find_element(*self.CONTACT_ACCOUNT_SEARCH).send_keys(acc_name)

    def selectContactAccName(self):
        self.driver.find_element(*self.CONTACT_1ST_ACC_SEARCH).click()

    def clickSaveContact(self):
        self.driver.find_element(*self.CONTACT_SAVE).click()
        time.sleep(2)

    def verifyCreatedContactName(self):
        self.driver.refresh()
        time.sleep(3)
        return self.driver.find_element(*self.CONTACT_FINAL_NAME).text
