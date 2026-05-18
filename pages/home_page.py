from .base_page import BasePage
from config.settings import USERNAME, PASSWORD, BASE_URL, LOGIN_PATH, HOME_PATH
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)