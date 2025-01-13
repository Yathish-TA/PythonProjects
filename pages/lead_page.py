import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LeadPage(BasePage):

    LEADS_DROPDOWN = (By.XPATH, "//a[@title='Leads']/following::a[@role='button'][1]")
    NEW_LEAD = (By.XPATH, "//span[text()='New Lead']")
    LEAD_LASTNAME = (By.XPATH, "//input[@name='lastName']")
    LEAD_COMPANY = (By.XPATH,"//input[@name='Company']")
    LEAD_SAVE = (By.XPATH,"//button[@name='SaveEdit']")
    LEAD_FINAL_NAME = (By.XPATH,"//*[@name='primaryField']/lightning-formatted-name")
    LEAD_CONVERT = (By.XPATH,"//button[@name='Convert']")
    CONVERT_LEAD_BUTTON = (By.XPATH,"(//button[text()='Convert'])[2]")
    CONVERTED_LEAD_TEXT = (By.XPATH,"(//h2[text()='Your lead has been converted'])")
    CLOSE_LEAD_WINDOW = (By.XPATH,"//button[@title='Close this window']")



    def clickLeadsDropDown(self):
        time.sleep(5)
        self.clickByLocator(self.LEADS_DROPDOWN)

    def clickNewLead(self):
        self.clickUsingAction(self.NEW_LEAD)

    def enterTheDetails(self,lastname,company):
        self.wait_for_element(self.LEAD_LASTNAME).send_keys(lastname)
        self.wait_for_element(self.LEAD_COMPANY).send_keys(company)

    def clickSaveLead(self):
        self.clickByLocator(self.LEAD_SAVE)


    def verifyCreatedLeadName(self):
        return self.wait_for_element(self.LEAD_FINAL_NAME).text

    def clickLeadConvert(self):
        self.clickByLocator(self.LEAD_CONVERT)

    def clickConvertButton(self):
        self.clickByLocator(self.CONVERT_LEAD_BUTTON)

    def verifyConvertedOrNot(self):
        return self.wait_for_element(self.CONVERTED_LEAD_TEXT).text

    def isUserOnLeadPage(self):
       return self.wait_for_element(self.LEAD_FINAL_NAME)
