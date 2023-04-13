import pytest
from Tests import readExcelFile
from pageObject.login_page import loginPage
from pageObject.logout_page import logoutPage

@pytest.fixture
def test_login_user(driver):
    """
       Test : A user with valid credentials should be able to login successfully
       URL : https://login-app-iota.vercel.app
    """

    # Open Browser
    login_page = loginPage(driver)
    logout_page = logoutPage(driver)
    # Navigate to Site URL
    login_page.open()
    # Login to the page
    username = readExcelFile.read_data(4, 1)
    password = readExcelFile.read_data(4, 2)
    head_text = readExcelFile.read_data(4, 3)
    login_page.perform_login(username, password)
    # Validate logged in URL
    assert login_page.current_url == "https://login-app-iota.vercel.app/dashboard"
    # Validate login message
    assert login_page.is_dashboarHeading_text_displayed(), 'Invalid Credentials'
    assert login_page.dashboarHeading_text == head_text, "The login text is not matched"

    # # logout the page
    # logout_page.logout_action()
    #
    # # Check the URL
    # assert login_page.current_url == "https://login-app-iota.vercel.app/login"

def test_verify_contact_is_not_shown(driver, test_login_user):
    """
           Test : The contact menu should not be displayed to the non-admin user
           URL : https://login-app-iota.vercel.app
    """
    login_page = loginPage(driver)
    assert login_page.contact_not_found == True, "Contact menu is displayed"