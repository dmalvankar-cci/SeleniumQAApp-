import time

import pytest
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Tests import test_about, readExcelFile
from globalConstants import tasksUrl
from pageObject.login_page import loginPage
from pageObject.tasks_page import tasksPage



@pytest.fixture
def test_tasks_menu_verification(driver):
    """
    Test : Verify if the task tracker is opened onclick of Tasks menu
    URL : https://login-app-iota.vercel.app/task
    """
    # Use the page objects
    tasks_page = tasksPage(driver)
    login_page = loginPage(driver)

    # Loggin in
    test_about.test_about_us_heading_verify(driver)

    # Importing task page head text
    head_text = readExcelFile.read_data(2, 3)

    # Click on the Tasks menu
    tasks_page.hit_tasks()

    # Verify the URL
    assert login_page.current_url == tasksUrl

    # Verify the heading
    assert tasks_page.is_heading_text_displayed(), 'text is not there'
    assert tasks_page.heading_text == head_text, "The heading text is not matched"


    # Verify the Instructions are shown
    assert tasks_page.is_instruction_text_displayed(), 'Instruction is not displayed'






def test_addEmpty_task(test_tasks_menu_verification, driver):



    """
    Test : Verify if the "Fill today's time sheet" text is already entered in the text field
    Remove the text and validate the alert error message
    URL : https://login-app-iota.vercel.app/task
    """
    tasks_page = tasksPage(driver)

    # Remove the "Fill today's time sheet" from the text field
    tasks_page.remove_placeholder()
    
    """
    # For chrome
    # tasks_page.pass_task('test')
    
   
    # Hit the add button with the "test" text field
    # tasks_page.click_add()
    """



    # Hit the add button with the empty text field
    tasks_page.click_add()

    # Valid the alert error is shown
    wait = WebDriverWait(driver, 10)
    alert = wait.until(expected_conditions.alert_is_present())
    assert alert.text == "Please add the task! Task can't be empty", "alert text is not matched"

    # click ok from alert
    Alert(driver).accept()






# @pytest.mark.parametrize("task_name",
# [("My first task")])
@pytest.fixture
def test_add_first_task(test_tasks_menu_verification, driver):

    """
    Test : Add task as "My first task"
    URL : https://login-app-iota.vercel.app/task
    """
    tasks_page = tasksPage(driver)

    # Remove the "Fill today's time sheet" from the text field
    tasks_page.remove_placeholder()

    # Enter "My first task" in the text field
    tasks_page.pass_task("My first task")

    # click Add button
    tasks_page.click_add()

    tasks_page.is_first_record_displayed()


@pytest.fixture
def test_new_record_visibility(driver,test_add_first_task):
    """
    Test : Verify the added task is recorded and shown below the field and Instructions arent displayed
    URL : https://login-app-iota.vercel.app/task
    """
    tasks_page = tasksPage(driver)
    # Verify the Instructions aren't displayed
    assert tasks_page.is_instruction_visible == True, "Instructions are not hidden"
    # Verify the newly added record is shown below
    assert tasks_page.is_first_record_displayed(), "The first record is not displayed"
    assert tasks_page.first_record == "My first task", "record one is not proper"


@pytest.fixture
def test_action_icons_visibility(driver, test_new_record_visibility):
    """
    Test : Verify the edit, done, delete icons are shown with the record
    URL : https://login-app-iota.vercel.app/task
    """
    # Verify the edit, done, delete icons are displayed
    tasks_page = tasksPage(driver)
    assert tasks_page.is_action_icons_displayed == 3, "Didnt find the all icons"


@pytest.fixture
def test_verify_editing_record(driver,test_action_icons_visibility):

    """
    Test : Verify onclick of edit user can edit the record
    URL : https://login-app-iota.vercel.app/task
    """

    # Click on the edit icon
    tasks_page = tasksPage(driver)
    tasks_page.verify_edit()
    # Change "My first task" to ""My Second task"
    tasks_page.remove_placeholder()
    tasks_page.pass_task("My Second Task")
    # Click Save
    tasks_page.click_save()
    # Verify if the record is updated
    assert tasks_page.updated_text_is_displayed(), "The updated text isnt displayed"
    assert tasks_page.updated_text == "My Second Task", "The text is not updated"



def test_verify_done_record(driver, test_verify_editing_record):

    """
    Test : Verify onclick of done the task gets strikethrough
    URL : https://login-app-iota.vercel.app/task
    """

    # Click on the done icon
    tasks_page = tasksPage(driver)
    tasks_page.click_done()

    # Verify if the record is strikethrough
    assert tasks_page.verify_strikethrough() == "line-through", "The strikethrough is not done"







def test_verify_delete_record(driver,test_verify_editing_record):
    """
    Test : Verify onclick of delete the task gets deleted
    Test : Verify the edited/done record gets deleted
    URL : https://login-app-iota.vercel.app/task
    """

    # Click on the delete icon
    tasks_page = tasksPage(driver)
    tasks_page.click_delete()

    # Verify if the record is deleted instructions should be shown
    assert tasks_page.is_instruction_text_displayed(), "The single record is not deleted"

@pytest.fixture
def test_add_multiple_records(driver, test_action_icons_visibility):
    """
    test : verify adding multiple records 2-3
    url : https://login-app-iota.vercel.app/task
    """

    # enter "My third task" in the text field
    tasks_page = tasksPage(driver)
    tasks_page.pass_task("My third task")
    # click add button
    tasks_page.click_add()

    # verify the newly added records are shown below
    assert tasks_page.is_third_record_displayed(), "The third record isnt displayed"
    assert tasks_page.third_record == "My third task", "record three is not proper"

    # enter "My fourth task" in the text field
    tasks_page.pass_task("My fourth task")
    # click add button
    tasks_page.click_add()
    # verify the newly added records are shown below
    assert tasks_page.is_fourth_record_displayed(), "The fourth record isnt displayed"
    assert tasks_page.fourth_record == "My fourth task", "record four is not proper"

    # enter "My fifth task" in the text field
    tasks_page.pass_task("My fifth task")
    # click add button
    tasks_page.click_add()
    # verify the newly added records are shown below
    assert tasks_page.is_fifth_record_displayed(), "The fifth record isnt displayed"
    assert tasks_page.fifth_record == "My fifth task", "record five is not proper"

    # verify the instructions arent displayed
    assert tasks_page.is_instruction_visible == True, "Instructions are not hidden"


@pytest.mark.testme
def test_actions_work_with_multiple_records(driver,test_add_multiple_records ):
    """
    Test : Verify edit, done, delete icons are working if multiple records 2-3 are present
    URL : https://login-app-iota.vercel.app/task
    """
    # Click on the Tasks menu
    # Verify the URL
    # Verify the heading
    # Verify the newly added records are shown below
    tasks_page = tasksPage(driver)
    # Edit "My third task" to "My third-edited task"
    tasks_page.third_record_edit_click()
    tasks_page.remove_placeholder()
    tasks_page.pass_task("My third-edited task")

    # Click Save
    tasks_page.click_save()

    # Verify the updated task is shown
    assert tasks_page.updated_text_is_displayed_for_third_record(), "The updated text isnt displayed"
    assert tasks_page.updated_text_for_third_record == "My third-edited task", "The text is not updated"

    # click done for the "My fourth task"
    tasks_page.fourth_record_done_click()

    # Verify if the "My fourth task" got strikethrough
    tasks_page.verify_strikethrough_for_four_record()

    assert tasks_page.verify_strikethrough_for_four_record() == "line-through", "The strikethrough is not done"

    # delete the "My fifth task"
    tasks_page.fifth_record_delete_click()

    # Verify if the "My fifth task" is deleted from records
    assert tasks_page.verify_deletion_for_fifth_record == True, "The record is not deleted"
