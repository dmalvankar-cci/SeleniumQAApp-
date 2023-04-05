# Import packages
import pytest
from pageObject.about_page import aboutPage
from pageObject.home_page import homePage
from pageObject.login_page import loginPage



@pytest.mark.parametrize("username, password, head_text",
[("admin", "admin123", "Contact List")])
def test_home_link_verify(driver, head_text, username, password):
    """
       Test : Validate if onlick of home link it opens the home page
       Test : Verify the heading from the home page
       URL : https://login-app-iota.vercel.app
    """
    # Use the page objects
    home_page = homePage(driver)
    login_page = loginPage(driver)
    about_page = aboutPage(driver)

    # Navigate to the site
    login_page.open()

    # Login to the site
    login_page.perform_login(username, password)

    # Click another menu
    about_page.hit_about()

    # Verify other menu is opened
    assert login_page.current_url == "https://login-app-iota.vercel.app/about"

    # Click on the home link
    home_page.hit_home()

    # Validate URL
    assert login_page.current_url == "https://login-app-iota.vercel.app/dashboard"

    # Validate login message
    assert login_page.is_dashboarHeading_text_displayed(), 'Invalid Credentials'
    assert login_page.dashboarHeading_text == head_text, "The login text is not matched"


@pytest.mark.parametrize("username, password, head_text",
[("admin", "admin123", "Contact List")])
def test_logo_click_verify(driver, head_text, username, password):

    """
    Test : Verify if the logo is present in the header and onclick it redirects to home page
    URL : https://login-app-iota.vercel.app/dashboard
    """
    # Use the page objects
    home_page = homePage(driver)
    login_page = loginPage(driver)
    about_page = aboutPage(driver)

    # Navigate to the site
    login_page.open()

    # Login to the site
    login_page.perform_login(username, password)

    # Click another menu
    about_page.hit_about()


    # Verify other menu is opened
    assert login_page.current_url == "https://login-app-iota.vercel.app/about"

    # Click on the logo
    home_page.hit_logo()

    # Verify the URL
    assert login_page.current_url == "https://login-app-iota.vercel.app/dashboard"



