from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# import logging

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout = 10)
        # self.logger = logging.getLogger(__name__)

    def get_element(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            raise AssertionError(f"Element {locator} not found or not visible.")

    def get_elements(self, locator):
        try:
            elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
            return elements
        except TimeoutException:
            raise AssertionError(f"Elements {locator} not found or not visible.")

    def click(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except TimeoutException:
            raise AssertionError(f"Element {locator} not found or not clickable.")

    def send_keys(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            raise AssertionError(f"Element {locator} not found or not visible.")

    def url_contains_path(self, path):
        try:
            self.wait.until(EC.url_contains(path))
        except TimeoutException:
            raise AssertionError(f"The current URL does not contain the path '{path}'.")

    def element_contains_text(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element {locator} not found.")

        try:
            self.wait.until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            raise AssertionError(f"Expected text '{text}' but found '{element.text}' in element {locator}.")

    def assert_visibility_of_element(self, locator, element_name):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"'{element_name}' is not visible.")