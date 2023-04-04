import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pageObject.contact_page import contactPage
from pageObject.login_page import loginPage
from pageObject.logout_page import logoutPage


@pytest.mark.testme
# @pytest.fixture(params=["username", "password", "head_text"], ids=["admin", "admin123", "TASK TRACKER"])
# @pytest.fixture(params=["admin", "admin123", "TASK TRACKER"])
# @pytest.mark.parametrize("username, password, head_text",
# [("admin", "admin123", "TASK TRACKER")])
def test_contact_menu_verification(driver):
    """
    Test : Verify if the task tracker is opened onclick of Tasks menu
    URL : https://login-app-iota.vercel.app/task
    """
    # Use the page objects
    contact_page = contactPage(driver)
    login_page = loginPage(driver)
    logout_page = logoutPage(driver)

    # Navigate to the site
    login_page.open()

    # Login to the site
    login_page.perform_login("admin", "admin123")

    # Click on the Contact menu
    contact_page.hit_contact()

    # Verify the URL
    assert login_page.current_url == "https://login-app-iota.vercel.app/contact"

    # Verify the heading
    assert contact_page.is_heading_text_displayed(), 'text is not there'
    assert contact_page.contact_heading_text == "ADD CONTACTS", "The heading text is not matched"

    # Verify the table and records are shown
    assert contact_page.is_contact_table_displayed(), 'table is not there'





@pytest.mark.validate_contact_page
def test_contact_form():
    """
    Test : A user is logged in and navigating to the contact form thru the menu
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

    # Click on the contact menu
    contact_menu = driver.find_element(By.LINK_TEXT, 'Contact')
    contact_menu.click()

    # Validate the contact page URl
    contact_url = driver.current_url
    assert contact_url == "https://login-app-iota.vercel.app/contact", "The contact page URL is not matched"

    # Validate the contact menu is active
    menu_color = contact_menu.value_of_css_property('color')
    assert menu_color == 'rgba(255, 255, 255, 0.56)', "The active link color is not matched"

    time.sleep(3)
    driver.quit()

@pytest.mark.form_submission
def test_contact_form_submission():
    """
    Test : A user is logged in and filling the contact form and submits the form
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

    # Click on the contact menu
    contact_menu = driver.find_element(By.LINK_TEXT, 'Contact')
    contact_menu.click()

    # Validate the contact page URl
    contact_url = driver.current_url
    assert contact_url == "https://login-app-iota.vercel.app/contact", "The contact page URL is not matched"

    # Validate the contact menu is active
    menu_color = contact_menu.value_of_css_property('color')
    assert menu_color == 'rgba(255, 255, 255, 0.56)', "The active link color is not matched"

    # Locate the form fields
    name = driver.find_element(By.ID, 'name_textbox')
    email = driver.find_element(By.ID, 'email_textbox')
    phone = driver.find_element(By.ID, 'phone_textbox')
    msg = driver.find_element(By.ID, 'message_textbox')

    # Locate submit button
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # Enter data in the form fields
    name.send_keys("test")
    email.send_keys('test@test.com')
    phone.send_keys('9767941202')
    msg.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")


    # Submit the form
    submit_btn.click()

    # Validate the URL
    dashboard_url = driver.current_url
    assert dashboard_url == "https://login-app-iota.vercel.app/dashboard", "The dashboard URL is not matched"

    # Validate the text from the page
    page_heading = driver.find_element(By.CSS_SELECTOR, '.text-center.text-primary.mb-3')
    page_heading_text = page_heading.text
    assert page_heading.is_displayed(), "The dashboard page heading is not present"
    assert page_heading_text == "Contact List", "The page heading text is not matched"
    time.sleep(3)
    driver.quit()

@pytest.mark.table_check
def test_outputOfFormSubmission():
    """
    Test : After contact form submission checking if the details are stored in the table
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

    # Click on the contact menu
    contact_menu = driver.find_element(By.LINK_TEXT, 'Contact')
    contact_menu.click()

    # Validate the contact page URl
    contact_url = driver.current_url
    assert contact_url == "https://login-app-iota.vercel.app/contact", "The contact page URL is not matched"

    # Validate the contact menu is active
    menu_color = contact_menu.value_of_css_property('color')
    assert menu_color == 'rgba(255, 255, 255, 0.56)', "The active link color is not matched"

    # Locate the form fields
    name = driver.find_element(By.ID, 'name_textbox')
    email = driver.find_element(By.ID, 'email_textbox')
    phone = driver.find_element(By.ID, 'phone_textbox')
    msg = driver.find_element(By.ID, 'message_textbox')

    # Locate submit button
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # Enter data in the form fields
    name.send_keys("test")
    email.send_keys('test@test.com')
    phone.send_keys('9767941202')
    msg.send_keys(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

    # Submit the form
    submit_btn.click()

    # Validate the URL
    dashboard_url = driver.current_url
    assert dashboard_url == "https://login-app-iota.vercel.app/dashboard", "The dashboard URL is not matched"

    # Validate the text from the page
    page_heading = driver.find_element(By.CSS_SELECTOR, '.text-center.text-primary.mb-3')
    page_heading_text = page_heading.text
    assert page_heading.is_displayed(), "The dashboard page heading is not present"
    assert page_heading_text == "Contact List", "The page heading text is not matched"

    # Get the column count and validate
    table_colmns = driver.find_elements(By.XPATH, "//*[@class= 'table']/thead/tr/th")
    assert len(table_colmns) == 4, "The column count is not matched"

    # Get the row count and validate
    table_rows= driver.find_elements(By.XPATH, "//*[@class= 'table']/tbody/tr")
    assert len(table_rows) == 1, "The row count is not matched"

    time.sleep(2)
    driver.quit()
