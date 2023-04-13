# Import packages
import pytest

from globalConstants import dashboardUrl, loginUrl
from pageObject import about_page
from pageObject.login_page import loginPage
from pageObject.logout_page import logoutPage


@pytest.mark.parametrize("username,password,loggedIn_msg",
[("admin","admin123","Contact List")])
@pytest.mark.logout_user
def test_logout_user(driver,username,password,loggedIn_msg):
    """
    Test : A user with valid credentials should be able to login successfully and logout successfully
    URL : https://login-app-iota.vercel.app
    """
    # Open Browser
    login_page = loginPage(driver)
    logout_page = logoutPage(driver)
    # Navigate to Site URL
    login_page.open()
    # Login to the page
    login_page.perform_login(username, password)
    # Validate logged in URL
    assert login_page.current_url == dashboardUrl
    # Validate login message
    assert login_page.is_dashboarHeading_text_displayed(), 'Invalid Credentials'
    assert login_page.dashboarHeading_text == loggedIn_msg, "The login text is not matched"
    # logout the page
    logout_page.logout_action()
    # Check the URL
    assert login_page.current_url == loginUrl