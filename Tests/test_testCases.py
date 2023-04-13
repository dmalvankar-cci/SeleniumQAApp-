import pytest

from globalConstants import testcasesUrl
from pageObject.login_page import loginPage
from pageObject.testCases_page import testCasesPage
from Tests import test_about

@pytest.fixture
def test_verify_testcases_menu(driver):
    """
    Test : Verify if the Test cases page is opened onclick of Test-Cases menu
    URL : https://login-app-iota.vercel.app/test-cases
    """
    # Loggin in
    test_about.test_about_us_heading_verify(driver)

    # Click on the Test-Cases menu
    testCases_page = testCasesPage(driver)
    testCases_page.hit_testCases_menu()

    # Verify the URL
    login_page = loginPage(driver)
    assert login_page.current_url == testcasesUrl

    # Verify the 4 test cases are shown
    assert testCases_page.is_test_one_is_displayed(), "Test first isnt displayed"
    assert testCases_page.text_of_testStepsOne == "Test 1 : A user with valid credentials should able to Login successfully\nURL : https://login-app-iota.vercel.app/login"
    assert testCases_page.is_test_two_is_displayed(), "Test second isnt displayed"
    assert testCases_page.is_test_three_is_displayed(), "Test third isnt displayed"
    assert testCases_page.is_test_four_is_displayed(), "Test fourth isnt displayed"


@pytest.fixture
def test_verify_testCases_expand(driver,test_verify_testcases_menu):
    """
    Test : Verify onclick of any of the Test cases it expands the tab with test-steps
    URL : https://login-app-iota.vercel.app/test-cases
    """

    # Click on the first test cases
    testCases_page = testCasesPage(driver)
    testCases_page.hit_testOne()

    # Verify if test steps are shown
    assert testCases_page.total_testSteps_verify == 11, "The teststeps count is wrong"



def test_verify_testCases_collapse(driver, test_verify_testCases_expand):
    """
    Test : Verify onclick of any of the expanded Test cases it collapse the tab
    URL : https://login-app-iota.vercel.app/test-cases
    """

    # Click on the collapse button
    testCases_page = testCasesPage(driver)
    testCases_page.testSteps_one_collapse()

    # Verify if the testcase is collapsed
    assert testCases_page.are_testSteps_visible == False, "The teststeps are gone"


def test_validate_expand_collapse(driver, test_verify_testCases_expand):
    """
    Test : Verify at a time only one test case can be expanded 
    URL : https://login-app-iota.vercel.app/test-cases
    """

    # Click on the second test case
    testCases_page = testCasesPage(driver)
    testCases_page.hit_testTwo()

    # Verify if the first test is collapsed and second test case is expanded
    assert testCases_page.are_testSteps_visible == False, "The teststeps are gone"
    assert testCases_page.total_testSteps_verify_for_TC2 == 14, "The teststeps count is wrong"








