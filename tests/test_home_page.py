from pages.home_page import HomePage

def test_home_page(logged_driver):
    page = HomePage(logged_driver)
    page.url_contains_path("index")