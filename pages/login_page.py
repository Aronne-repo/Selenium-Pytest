from .base_page import BasePage
from config.settings import USERNAME, PASSWORD, BASE_URL, LOGIN_PATH, HOME_PATH
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    INPUT_USERNAME = (By.XPATH, "//input[@name='username']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, text):
        self.send_keys(self.INPUT_USERNAME, text)

    def enter_password(self, text):
        self.send_keys(self.INPUT_PASSWORD, text)

    def submit(self):
        self.click(self.LOGIN_BUTTON)

    def login(self):
        self.driver.get(BASE_URL + LOGIN_PATH)
        self.enter_username(USERNAME)
        self.enter_password(PASSWORD)
        self.submit()
        self.url_contains_path(HOME_PATH)