
import time
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("username,password,expected_error_msg",
[("incorrectUser","Password123","Invalid Credentials"),
("student","incorrectPassword","Invalid Credentials"),
("xyz","xyz","Invalid Credentials")])
@pytest.mark.invalid_username_password
def test_invalid_username_password(driver,username,password,expected_error_msg):
    """
    Test : A user with invalid username should not able to login 
    URL : https://login-app-iota.vercel.app
    """


    # Navigate to Site URL
    driver.get("https://login-app-iota.vercel.app")
    time.sleep(3)

    # Validate if default URL is pointing to login route
    url = driver.current_url
    assert url == "https://login-app-iota.vercel.app/login", "The url is not matching with the expected one"

    # locate username element
    uname = driver.find_element(By.ID, 'username_textbox')

    # locate password element
    passwrd = driver.find_element(By.ID, 'password_textbox')

    # locate Login button
    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # enter INValid username
    uname.send_keys(username)

    # enter valid password
    passwrd.send_keys(password)

    # click on login button
    login_btn.click()

    # Validate logged in URL
    no_logged_url = driver.current_url
    assert no_logged_url == "https://login-app-iota.vercel.app/login", "The URL is not matching with the About URL"

    # Validate login error message
    login_error_msg = driver.find_element(By.XPATH, "//div[@class='text-center text-danger mb-2']")
    login_error_txt = login_error_msg.text
    assert login_error_msg.is_displayed(), 'Invalid Credentials'
    assert login_error_txt == expected_error_msg, "The login error is not matched"

    time.sleep(3)


@pytest.mark.valid_login
def test_valid_login(self, driver):
    """
    Test : A user with valid credentials should be able to login successfully
    URL : https://login-app-iota.vercel.app
    """

    # Navigate to Site URL
    driver.get("https://login-app-iota.vercel.app")
    time.sleep(3)

    # Validate if default URL is pointing to login route
    url = driver.current_url
    assert url == "https://login-app-iota.vercel.app/login", "The url is not matching with the expected one"


    # locate username element
    uname = driver.find_element(By.ID, 'username_textbox')

    # locate password element
    passwrd = driver.find_element(By.ID, 'password_textbox')

    # locate Login button
    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # enter Valid username
    uname.send_keys('admin')

    # enter valid password
    passwrd.send_keys('admin123')

    # click on login button
    login_btn.click()

    # Validate logged in URL
    about_url = driver.current_url
    assert about_url == "https://login-app-iota.vercel.app/about", "The URL is not matching with the About URL"

    # Validate login message
    login_msg = driver.find_element(By.XPATH, "//h1[normalize-space()='Welcome to Selenium Learning Group']")
    login_txt = login_msg.text
    assert login_msg.is_displayed(), "The welcome message is not displayed"
    assert login_txt == "Welcome to Selenium Learning Group", "The login text is not matched"

    time.sleep(3)







