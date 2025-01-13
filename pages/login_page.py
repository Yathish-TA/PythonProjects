from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_URL = "https://login.salesforce.com"
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "Login")
    DASHBOARD_INDICATOR = (By.XPATH, "//span[@title='Sales']")

    def open(self):
        self.browser.get(self.LOGIN_URL)

    def login(self, username, password):
        self.wait_for_element(self.USERNAME_INPUT).send_keys(username)
        self.wait_for_element(self.PASSWORD_INPUT).send_keys(password)
        self.clickByLocator(self.LOGIN_BUTTON)

    def is_dashboard_displayed(self):
        return self.wait_for_element(self.DASHBOARD_INDICATOR)