import time
import pytest

from pageObject import login_page
from pageObject.about_page import aboutPage
from pageObject.login_page import loginPage



@pytest.mark.parametrize("username, password, head_text",
[("admin", "admin123", "Welcome to Selenium Learning Group")])
def test_about_us_heading_verify(driver, head_text, username, password):
    about_page = aboutPage(driver)
    login_page = loginPage(driver)
    login_page.open()
    login_page.perform_login(username, password)
    about_page.hit_about()
    assert login_page.current_url == "https://login-app-iota.vercel.app/about"
    assert about_page.is_heading_text_displayed(), 'text is not there'
    assert about_page.heading_text == head_text, "The heading text is not matched"
    about_page.logout_action()
    assert login_page.current_url == "https://login-app-iota.vercel.app/login"