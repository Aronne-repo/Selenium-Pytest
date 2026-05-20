from pages.home_page import HomePage

def test_home_page(logged_driver):
    page = HomePage(logged_driver)
    page.assert_visibility_of_logo()
    page.assert_dashboard_title("Dashboard")

def test_user_dropdown(logged_driver):
    page = HomePage(logged_driver)
    page.open_user_dropdown()
    assert page.get_user_dropdown_options() == ["About", "Support", "Change Password", "Logout"]

def test_sidebar_search(logged_driver):
    page = HomePage(logged_driver)
    page.open_sidebar_chevron()
    page.search_in_sidebar("My Info")
    assert "My Info" in page.get_sidebar_search_results()