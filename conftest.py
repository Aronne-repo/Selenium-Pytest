from pages.login_page import LoginPage
from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def logged_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    page = LoginPage(driver)
    page.login()
    yield driver
    driver.quit()