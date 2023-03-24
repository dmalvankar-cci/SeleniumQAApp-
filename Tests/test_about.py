import time
import pytest
from selenium.webdriver.common.by import By

from pageObject.about_page import aboutPage
from pageObject.login_page import loginPage
@pytest.mark.parametrize("head_text",
[("Welcome to Selenium Learning Group")])
def about_us_heading_verify(driver, headingTxt):
    about_page = aboutPage(driver)
    about_page.open()
    about_page.about_action()
    time.sleep(5)
    assert about_page.current_url == "https://login-app-iota.vercel.app/about"
    assert about_page.is_heading_text_displayed(), 'text is not there'
    assert about_page.heading_text == headingTxt, "The heading text is not matched"
    about_page.logout_action()
    assert about_page.current_url == "https://login-app-iota.vercel.app"