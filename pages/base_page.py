from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((locator)))

    def clickByLocator(self, locator, timeout=10):
        element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((locator)))
        element = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((locator)))
        element.click()
    def clickUsingAction(self,locator):
        element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((locator)))
        action = ActionChains(self.browser)
        action.click(on_element=element).perform()


    def click_element(self,locator, timeout=10):
        element = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((locator)))
        ActionChains(self.browser).move_to_element(element).click().perform()

    def js_click(self, by, locator, timeout=10):
        element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((by, locator)))
        self.browser.execute_script("arguments[0].click();", element)
