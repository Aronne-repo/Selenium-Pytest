from pages.login_page import LoginPage

def test_login(driver):
    page = LoginPage(driver)
    page.login()