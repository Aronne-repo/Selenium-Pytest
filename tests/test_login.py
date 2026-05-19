from pages.login_page import LoginPage
from config.settings import HOME_PATH

def test_login(driver):
    page = LoginPage(driver)
    
    page.login()
    page.url_contains_path(HOME_PATH)