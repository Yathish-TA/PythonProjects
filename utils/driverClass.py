from selenium import webdriver

def get_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)  # Ensure chromedriver is in PATH
    return driver