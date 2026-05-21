from pages.home_page import HomePage
from config.settings import HOME_PATH

def test_logout(logged_driver):
    page = HomePage(logged_driver)
    page.url_contains_path(HOME_PATH)
    page.open_user_dropdown()
    page.do_logout()