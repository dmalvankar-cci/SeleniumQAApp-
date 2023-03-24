# Import packages
import pytest
from pageObject.about_page import aboutPage
from pageObject.login_page import loginPage
from pageObject.logout_page import logoutPage


@pytest.mark.parametrize("username, password, head_text",
[("admin", "admin123", "Welcome to Selenium Learning Group")])
def test_about_us_heading_verify(driver, head_text, username, password):
    """
       Test : Validate if onlick of about link it opens the about page
       Test : Verify the heading from the about page and logout
       Test : Validate if onlick of logout link it logouts the user
       URL : https://login-app-iota.vercel.app
    """
    # Use the page objects
    about_page = aboutPage(driver)
    login_page = loginPage(driver)
    logout_page = logoutPage(driver)
    # Navigate to the site
    login_page.open()

    # Login to the site
    login_page.perform_login(username, password)

    # Hit the about link
    about_page.hit_about()

    # Check the heading with URL
    assert login_page.current_url == "https://login-app-iota.vercel.app/about"
    assert about_page.is_heading_text_displayed(), 'text is not there'
    assert about_page.heading_text == head_text, "The heading text is not matched"

    # logout the page
    logout_page.logout_action()

    # Check the URL
    assert login_page.current_url == "https://login-app-iota.vercel.app/login"