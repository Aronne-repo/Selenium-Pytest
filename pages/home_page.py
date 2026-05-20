from .base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    LOGO = (By.XPATH, "//img[contains(@src, 'orangehrm-logo.png')]")
    DASHBOARD_TITLE = (By.CLASS_NAME, "oxd-topbar-header-breadcrumb-module")
    USER_NAME = (By.CLASS_NAME, "oxd-userdropdown-name")
    USER_DROPDOWN_ARROW = (By.CLASS_NAME, "oxd-userdropdown-icon")
    USER_DROPDOWN_OPTIONS = (By.XPATH, "//ul[@class='oxd-dropdown-menu' and @role='menu']//a[@role='menuitem']")
    SIDEBAR_CHEVRON = (By.XPATH, "//i[contains(@class,'bi-chevron-')]")
    SIDEBAR_SEARCH_BAR = (By.CLASS_NAME, "oxd-input")
    SIDEBAR_OPTIONS = (By.XPATH, "//li[@class='oxd-main-menu-item-wrapper']")

    def __init__(self, driver):
        super().__init__(driver)

    def assert_visibility_of_logo(self):
        self.assert_visibility_of_element(self.LOGO, "Orange HRM logo")

    def assert_dashboard_title(self, text):
        self.element_contains_text(self.DASHBOARD_TITLE, text)

    def assert_user_name(self, text):
        self.element_contains_text(self.USER_NAME, text)

    def open_user_dropdown(self):
        self.click(self.USER_DROPDOWN_ARROW)

    def get_user_dropdown_options(self):
        dropdown_options = self.get_elements(self.USER_DROPDOWN_OPTIONS)
        return [option.text for option in dropdown_options]

    def open_sidebar_chevron(self):
        element = self.get_element(self.SIDEBAR_CHEVRON)
        classes = element.get_attribute("class").split()
        if "toggled" in classes:
            self.click(element.find_element(By.XPATH, "./parent::button"))

    def close_sidebar_chevron(self):
        element = self.get_element(self.SIDEBAR_CHEVRON)
        classes = element.get_attribute("class").split()
        if "toggled" not in classes:
            self.click(element.find_element(By.XPATH, "./parent::button"))

    def search_in_sidebar(self, text):
        self.send_keys(self.SIDEBAR_SEARCH_BAR, text)

    def get_sidebar_search_results(self):
        sidebar_options = self.get_elements(self.SIDEBAR_OPTIONS)
        return [option.text for option in sidebar_options]