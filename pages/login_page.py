from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.USERNAME_INPUT = (By.ID, "username")
        self.PASSWORD_INPUT = (By.ID, "password")
        self.LOGIN_BUTTON = (By.ID, "Login")
        self.DASHBOARD_INDICATOR = (By.XPATH, "//span[@title='Sales']")


    def open_login_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_dashboard_displayed(self):
        return self.driver.find_element(*self.DASHBOARD_INDICATOR).is_displayed()