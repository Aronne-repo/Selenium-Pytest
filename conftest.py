from selenium import webdriver
import pytest
import logging
from pages.login_page import LoginPage

def pytest_configure():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        force=True)

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture
def logged_driver(driver):
    page = LoginPage(driver)
    page.login()
    return driver