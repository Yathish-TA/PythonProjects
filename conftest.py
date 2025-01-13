import pytest

from utils.driverClass import get_browser

def before_all(context):
    context.browser = get_browser()

def after_all(context):
    context.browser.quit()