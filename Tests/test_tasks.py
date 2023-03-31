import pytest
from selenium.webdriver.common.alert import Alert
from pageObject.login_page import loginPage
from pageObject.logout_page import logoutPage
from pageObject.tasks_page import tasksPage


@pytest.fixture
# @pytest.fixture(params=["username", "password", "head_text"], ids=["admin", "admin123", "TASK TRACKER"])
# @pytest.fixture(params=["admin", "admin123", "TASK TRACKER"])
# @pytest.mark.parametrize("username, password, head_text",
# [("admin", "admin123", "TASK TRACKER")])
def test_tasks_menu_verification(driver):
    """
    Test : Verify if the task tracker is opened onclick of Tasks menu
    URL : https://login-app-iota.vercel.app/task
    """
    # Use the page objects
    tasks_page = tasksPage(driver)
    login_page = loginPage(driver)
    logout_page = logoutPage(driver)

    # Navigate to the site
    login_page.open()

    # Login to the site
    login_page.perform_login("admin", "admin123")

    # Click on the Tasks menu
    tasks_page.hit_tasks()

    # Verify the URL
    assert login_page.current_url == "https://login-app-iota.vercel.app/task"

    # Verify the heading
    assert tasks_page.is_heading_text_displayed(), 'text is not there'
    assert tasks_page.heading_text == "TASK TRACKER", "The heading text is not matched"


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

    # Hit the add button with the empty text field
    tasks_page.click_add()

    # Valid the alert error is shown
    assert Alert(driver).text == "Please add the task! Task can't be empty", "alert text is not matched"

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
    tasks_page.instruction_not_found()
    # Verify the newly added record is shown below
    tasks_page.is_first_record_displayed()


@pytest.fixture
def test_action_icons_visibility(driver, test_new_record_visibility):
    """
    Test : Verify the edit, done, delete icons are shown with the record
    URL : https://login-app-iota.vercel.app/task
    """
    # Verify the edit, done, delete icons are displayed
    tasks_page = tasksPage(driver)
    tasks_page.is_action_icons_displayed()

@pytest.mark.testme
def test_verify_editing_record(driver, test_new_record_visibility, test_action_icons_visibility):

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
    tasks_page.updated_text_is_displayed()
    tasks_page.updated_text == "My Second Task", "The text is not updated"


