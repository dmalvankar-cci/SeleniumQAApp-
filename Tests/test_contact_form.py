import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pageObject.contact_page import contactPage
from pageObject.login_page import loginPage
from pageObject.logout_page import logoutPage
from Tests import readExcelFile


@pytest.fixture
# @pytest.fixture(params=["username", "password", "head_text"], ids=["admin", "admin123", "TASK TRACKER"])
# @pytest.fixture(params=["admin", "admin123", "TASK TRACKER"])
# @pytest.mark.parametrize("username, password, head_text",
# [("admin", "admin123", "TASK TRACKER")])
def test_contact_menu_verification(driver):
    """
    Test : Verify if the task tracker is opened onclick of Tasks menu
    URL : https://login-app-iota.vercel.app/task
    """
    username = readExcelFile.read_data(2, 1)
    password = readExcelFile.read_data(2, 2)

    # Use the page objects
    contact_page = contactPage(driver)
    login_page = loginPage(driver)
    logout_page = logoutPage(driver)

    # Navigate to the site
    login_page.open()

    # Login to the site
    login_page.perform_login(username, password)

    # Click on the Contact menu
    contact_page.hit_contact()

    # Verify the URL
    assert login_page.current_url == "https://login-app-iota.vercel.app/contact"

    # Verify the heading
    assert contact_page.is_heading_text_displayed(), 'text is not there'
    assert contact_page.contact_heading_text == "ADD CONTACTS", "The heading text is not matched"

    # Verify the table and records are shown
    assert contact_page.is_contact_table_displayed(), 'table is not there'

    return contact_page.table_rows_count


@pytest.fixture
def test_form_is_opened(driver,test_contact_menu_verification):
    """
    Test : Verify onclick of add '+' button form is displayed with submit button
    URL : https://login-app-iota.vercel.app/contact
    """

    # Click on the '+'
    contact_page = contactPage(driver)
    contact_page.hit_plus_icon()

    # Verify if the all form fields are shown with submit button
    assert contact_page.is_form_fields_displayed == 5, "The all fields are not found"
    assert contact_page.is_submit_btn_displayed(), "Submit button isnt there"




def test_empty_form_submission(driver,test_form_is_opened):
    """
    Test : Verify empty form submission
    Test : Verify email field has validation
    URL : https://login-app-iota.vercel.app/contact
    """

    # Click on sumbit button without entering any data in the form
    contact_page = contactPage(driver)
    contact_page.hit_submit_btn()

    # Verify if the "First name" field got the error
    assert contact_page.verify_name_field_error == "Please fill out this field.", "The empty field error is not shown"





def test_validate_email_field(driver, test_form_is_opened):
    """
    Test : Validate the phone number and email field
    URL : https://login-app-iota.vercel.app/contact
    """
    fname = readExcelFile.read_data_for_contact_form(2,1)
    lname = readExcelFile.read_data_for_contact_form(2,2)
    email = readExcelFile.read_data_for_contact_form(2,3)
    phone = readExcelFile.read_data_for_contact_form(2,4)
    msg = readExcelFile.read_data_for_contact_form(2,5)
    # Enter "test" in all fields

    contact_page = contactPage(driver)
    contact_page.pass_data_in_fields(fname, lname, email, phone, msg)

    # Click Submit
    contact_page.hit_submit_btn()

    # Validate if the errors are shown for the email
    assert contact_page.verify_email_field_error == "Please include an '@' in the email address. 'test' is missing an '@'.", "The email field validation is not added"



@pytest.fixture
def test_verify_form_submission(driver,test_form_is_opened):
    """
    Test : Enter valid data in all fields and submit the form
    URL : https://login-app-iota.vercel.app/contact
    """
    fname = readExcelFile.read_data_for_contact_form(3, 1)
    lname = readExcelFile.read_data_for_contact_form(3, 2)
    email = readExcelFile.read_data_for_contact_form(3, 3)
    phone = readExcelFile.read_data_for_contact_form(3, 4)
    msg = readExcelFile.read_data_for_contact_form(3, 5)

    # Enter "test" in all fields except in email and phone number
    # Enter "test@test.com" in email field
    # Enter "9874512036" in phone number field'
    contact_page = contactPage(driver)
    contact_page.pass_data_in_fields(fname, lname, email, phone, msg)

    # Click submit
    contact_page.hit_submit_btn()

    # Verify the table and records are shown
    assert contact_page.is_contact_table_displayed(), 'table is not there'



def test_verify_table_records(driver, test_contact_menu_verification, test_verify_form_submission):
    """
    Test : Verify if the record is added in the table
    URL : https://login-app-iota.vercel.app/contact
    """
    # Verify the table and records are shown
    contact_page = contactPage(driver)
    contact_page.is_contact_table_displayed()

    # Verify if the above details are shown in the table as a new row
    initial_table_rows = test_contact_menu_verification
    assert contact_page.table_rows_count == initial_table_rows+1, "The row count is not matched"



