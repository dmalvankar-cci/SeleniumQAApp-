
import time
import pytest
from selenium.webdriver.common.by import By

from pageObject.login_page import loginPage


@pytest.mark.parametrize("username,password,loggedIn_msg",
[("admin","admin123","Contact List")])
@pytest.mark.valid_login_wd_page_object
def test_valid_login_pageObject(driver,username,password,loggedIn_msg):
    login_page = loginPage(driver)
    login_page.open()
    login_page.perform_login(username,password)
    assert login_page.current_url == "https://login-app-iota.vercel.app/dashboard"
    assert login_page.is_dashboarHeading_text_displayed(), 'Invalid Credentials'
    assert login_page.dashboarHeading_text == loggedIn_msg, "The login text is not matched"

@pytest.mark.parametrize("username,password,expectedErrorMsg",
[("xyz","admin123","Invalid Credentials")])
@pytest.mark.Invalid_login_wd_page_object
def test_invalid_login_pageObject(driver,username,password,expectedErrorMsg):
    login_page = loginPage(driver)
    login_page.open()
    login_page.perform_login(username,password)
    assert login_page.current_url == "https://login-app-iota.vercel.app/login"
    assert login_page.is_loginError_lable_displayed(), 'Invalid Credentials'
    assert login_page.loginError_lable_text == expectedErrorMsg, "The login error is not matched"















