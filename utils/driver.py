from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdrivermanager_cn import ChromeDriverManager


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.implicitly_wait(15)
    # driver.refresh()
    return driver

