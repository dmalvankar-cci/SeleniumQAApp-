
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.logout_user
def test_logout_user():
    """
    Test : A user with valid credentials should able to login successfully
    URL : https://login-app-iota.vercel.app
    """
    # Open Browser
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

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
    # locate logout menu/button
    logout_btn = driver.find_element(By.LINK_TEXT, 'Logout')

    # click on logout button
    logout_btn.click()

    # validate that login page URL is displayed
    login_page_url = driver.current_url
    assert login_page_url == "https://login-app-iota.vercel.app/login", "The URL is not matching with the About URL"

    time.sleep(3)

    driver.quit()

