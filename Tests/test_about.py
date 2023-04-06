# Import packages
from Tests import readExcelFile
from pageObject.about_page import aboutPage
from pageObject.login_page import loginPage
from pageObject.logout_page import logoutPage



def test_about_us_heading_verify(driver):
    """
       Test : Validate if onlick of about link it opens the about page
       Test : Verify the heading from the about page
       URL : https://login-app-iota.vercel.app
    """
    # Use the page objects
    about_page = aboutPage(driver)
    login_page = loginPage(driver)
    logout_page = logoutPage(driver)

    username = readExcelFile.read_data(2, 1)
    password = readExcelFile.read_data(2, 2)
    head_text = readExcelFile.read_data(3, 3)

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

    # # logout the page
    # logout_page.logout_action()
    #
    # # Check the URL
    # assert login_page.current_url == "https://login-app-iota.vercel.app/login"