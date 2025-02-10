import time
from selenium.webdriver.common.by import By


class OpportunitiesPage:

    def __init__(self, driver):
        self.driver = driver
        self.OPP_DROPDOWN = (By.XPATH, "//a[@title='Leads']/following::a[@role='button'][4]")
        self.NEW_OPP = (By.XPATH, "//span[text()='New Opportunity']")
        self.OPP_NAME = (By.XPATH, "//input[@name='Name']")
        self.OPP_ACCOUNT_SEARCH = (By.XPATH, "//input[@placeholder='Search Accounts...']")
        self.OPP_1ST_ACC_SEARCH = (By.XPATH, "//li[@class='slds-listbox__item'][1]")
        self.OPP_CLOSE_DATE = (By.XPATH, "//input[@name='CloseDate']")
        self.OPP_STAGE_DROPDOWN = (By.XPATH, "(//button[@aria-haspopup='listbox'])[1]")
        self.OPP_STAGE_OPTIONS = (By.XPATH, "//div[@aria-label='Stage']/lightning-base-combobox-item")
        self.OPP_FORECAST_CATEGORY = (By.XPATH, "//button[@aria-label='Forecast Category']")
        self.OPP_FORECAST_OPTIONS = (By.XPATH, "//div[@aria-label='Forecast Category']/lightning-base-combobox-item")
        self.OPP_SAVE = (By.XPATH, "//button[@name='SaveEdit']")
        self.OPP_FINAL_NAME = (By.XPATH, "(//slot[@name='primaryField']/lightning-formatted-text)")


    def clickOppDropDown(self):
        time.sleep(2)
        self.driver.find_element(*self.OPP_DROPDOWN).click()

    def clickNewOpp(self):
        element = self.driver.find_element(*self.NEW_OPP)
        self.driver.execute_script("arguments[0].click();", element)

    def enterOppName(self, Opp_name):
        self.driver.find_element(*self.OPP_NAME).send_keys(Opp_name)

    def enterOppAccountName(self, acc_name):
        self.driver.find_element(*self.OPP_ACCOUNT_SEARCH).clear()
        self.driver.find_element(*self.OPP_ACCOUNT_SEARCH).send_keys(acc_name)

    def selectOppAccountName(self):
        self.driver.find_element(*self.OPP_1ST_ACC_SEARCH).click()

    def enterCloseDate(self, date):
        self.driver.find_element(*self.OPP_CLOSE_DATE).send_keys(date)

    def selectOppStage(self, Opp_stage):
        element = self.driver.find_element(*self.OPP_STAGE_DROPDOWN)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        elements = self.driver.find_elements(*self.OPP_STAGE_OPTIONS)
        for opt in elements:
            if opt.text == Opp_stage:
                opt.click()
                break

    def selectOppForecast(self, Opp_forecast):
        element = self.driver.find_element(*self.OPP_FORECAST_CATEGORY)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        elements = self.driver.find_elements(*self.OPP_FORECAST_OPTIONS)
        for opt in elements:
            if opt.text == Opp_forecast:
                opt.click()
                break


    def clickSaveOpp(self):
        self.driver.find_element(*self.OPP_SAVE).click()
        time.sleep(2)

    def verifyCreatedOppName(self):
        self.driver.refresh()
        time.sleep(2)
        return self.driver.find_element(*self.OPP_FINAL_NAME).text
