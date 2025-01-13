import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.driverClass import get_browser


def before_all(context):
    print("Initializing browser...")
    context.browser = get_browser()
    print("Browser initialized:", context.browser)

def after_all(context):
    print("Closing browser...")
    context.browser.quit()
    print("Browser closed.")

