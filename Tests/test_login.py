# Import packages
import pytest
from pageObject.login_page import loginPage


@pytest.mark.parametrize("username,password,loggedIn_msg",
[("admin","admin123","Contact List")])
@pytest.mark.valid_login_wd_page_object
def test_valid_login_pageObject(driver,username,password,loggedIn_msg):
    """
    Test : A user with valid credentials should be able to login successfully
    URL : https://login-app-iota.vercel.app
    """
    # Open Browser
    login_page = loginPage(driver)
    # Navigate to Site URL
    login_page.open()
    # Login to the page
    login_page.perform_login(username, password)
    # Validate logged in URL
    assert login_page.current_url == "https://login-app-iota.vercel.app/dashboard"
    # Validate login message
    assert login_page.is_dashboarHeading_text_displayed(), 'Invalid Credentials'
    assert login_page.dashboarHeading_text == loggedIn_msg, "The login text is not matched"

@pytest.mark.parametrize("username,password,expectedErrorMsg",
[("xyz","admin123","Invalid Credentials"),
 ("admin","xyz","Invalid Credentials")])
@pytest.mark.Invalid_login_wd_page_object
def test_invalid_login_pageObject(driver,username,password,expectedErrorMsg):
    """
    Test : A user with invalid username should not able to login 
    Test : A user with invalid password should not able to login 
    URL : https://login-app-iota.vercel.app
    """
    # Open Browser
    login_page = loginPage(driver)
    # Navigate to Site URL
    login_page.open()
    # Login to the page
    login_page.perform_login(username,password)
    # Validate logged in URL
    assert login_page.current_url == "https://login-app-iota.vercel.app/login"
    # Validate login message
    assert login_page.is_loginError_lable_displayed(), 'Invalid Credentials'
    assert login_page.loginError_lable_text == expectedErrorMsg, "The login error is not matched"















