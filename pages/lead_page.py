import time
from selenium.webdriver.common.by import By


class LeadPage:

    def __init__(self, driver):
        self.driver = driver
        self.LEADS_DROPDOWN = (By.XPATH, "//a[@title='Leads']/following::a[@role='button'][1]")
        self.NEW_LEAD = (By.XPATH, "//span[text()='New Lead']")
        self.LEAD_LASTNAME = (By.XPATH, "//input[@name='lastName']")
        self.LEAD_COMPANY = (By.XPATH, "//input[@name='Company']")
        self.LEAD_SAVE = (By.XPATH, "//button[@name='SaveEdit']")
        self.LEAD_FINAL_NAME = (By.XPATH, "//*[@name='primaryField']/lightning-formatted-name")
        self.LEAD_CONVERT = (By.XPATH, "//button[@name='Convert']")
        self.CONVERT_LEAD_BUTTON = (By.XPATH, "(//button[text()='Convert'])[2]")
        self.CONVERTED_LEAD_TEXT = (By.XPATH, "(//h2[text()='Your lead has been converted'])")
        self.CLOSE_LEAD_WINDOW = (By.XPATH, "//button[@title='Close this window']")
        self.CLOSE_GO_TO_LEADS = (By.XPATH, "//button[text()='Go to Leads']")
        self.EXISTING_ACCOUNT = (By.XPATH, "//span[text()='Choose Existing Account']")
        self.EXISTING_ACCOUNT_TEXT_FILED = (By.XPATH, "//input[@title='Search for matching accounts']")
        self.ACCOUNT_LIST = (By.XPATH, "//div[@class='listContent']//li")
        self.LIST_FIRST_ACCOUNT = (By.XPATH, "//div[@class='listContent']//li[1]")

    def clickLeadsDropDown(self):
        time.sleep(3)
        self.driver.find_element(*self.LEADS_DROPDOWN).click()

    def clickNewLead(self):
        element = self.driver.find_element(*self.NEW_LEAD)
        self.driver.execute_script("arguments[0].click();", element)

    def enterTheDetails(self, lastname, company):
        self.driver.find_element(*self.LEAD_LASTNAME).send_keys(lastname)
        self.driver.find_element(*self.LEAD_COMPANY).send_keys(company)

    def clickSaveLead(self):
        self.driver.find_element(*self.LEAD_SAVE).click()
        time.sleep(3)

    def verifyCreatedLeadName(self):
        self.driver.refresh()
        time.sleep(3)
        return self.driver.find_element(*self.LEAD_FINAL_NAME).text

    def clickLeadConvert(self):
        self.driver.find_element(*self.LEAD_CONVERT).click()

    def clickConvertButton(self):
        time.sleep(2)
        self.driver.find_element(*self.CONVERT_LEAD_BUTTON).click()
        time.sleep(2)

    def verifyConvertedOrNot(self):
        return self.driver.find_element(*self.CONVERTED_LEAD_TEXT).text

    def closeLeadPopup(self):
        element = self.driver.find_element(*self.CLOSE_LEAD_WINDOW)
        self.driver.execute_script("arguments[0].click();", element)

    def isUserOnLeadPage(self):
        return self.driver.find_element(*self.LEAD_FINAL_NAME).isDisplayed()

    def newOrExistingAccount(self, type, AccName):
        if type == "New":
            pass
        elif type == "Existing":
            self.driver.find_element(*self.EXISTING_ACCOUNT).click()
            self.driver.find_element(*self.EXISTING_ACCOUNT_TEXT_FILED).send_keys(AccName)
            time.sleep(3)
            self.driver.find_element(*self.LIST_FIRST_ACCOUNT).click()
        else:
            print("Unsupported Value - Please Provide Either 'New' or 'Existing' value as a Type of Account")
            raise NotImplementedError
