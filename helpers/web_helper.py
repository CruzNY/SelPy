from selenium import webdriver

from helpers.helper_func import HelperFunc

def get_browser(browser):
    if browser == 'chrome':
        return HelperFunc(webdriver.Chrome())