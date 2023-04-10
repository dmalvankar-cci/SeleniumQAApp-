from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class testCasesPage:

    __tc_menu = (By.LINK_TEXT, "Test-Cases")
    __test_one = (By.ID, "flush-headingOne")
    __test_two = (By.XPATH, "//button[@data-bs-target='#flush-collapseTwo']")
    __test_three = (By.XPATH, "//button[@data-bs-target='#flush-collapseThree']")
    __test_four = (By.XPATH, "//button[@data-bs-target='#flush-collapseFour']")

    __testSteps_div1 = (By.XPATH, "//div[@id='flush-collapseOne']//p")
    __testSteps_div2 = (By.XPATH, "//div[@id='flush-collapseTwo']//p")


    __collapse_btn = (By.XPATH, "//button[@data-bs-target='#flush-collapseOne']")

    __testStep_one = (By.XPATH, "//div[@id='flush-collapseOne']//p[contains(text(),'1. Open Browser')]")
    __testStep_two = (By.XPATH, "//div[@id='flush-collapseOne']//p[contains(text(),'2. Navigate to Site URL')]")
    __testStep_five = (By.XPATH, "//div[@id='flush-collapseOne']//p[contains(text(),'5. Locate password element')]")
    __testStep_eight = (By.XPATH, "//div[@id='flush-collapseOne']//p[contains(text(),'8. Enter valid password')]")
    __testStep_ten = (By.XPATH, "//div[@id='flush-collapseOne']//p[contains(text(),'10. Validate logged in URL')]")

    def __init__(self,driver:WebDriver):
        self._driver = driver

    def hit_testCases_menu(self):
        self._driver.find_element(*self.__tc_menu).click()

    def is_test_one_is_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__test_one))
        testOne = self._driver.find_element(*self.__test_one)
        return testOne.is_displayed()


    def is_test_two_is_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__test_two))
        testTwo = self._driver.find_element(*self.__test_two)
        return testTwo.is_displayed()

    def is_test_three_is_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__test_three))
        testThree = self._driver.find_element(*self.__test_three)
        return testThree.is_displayed()
    def is_test_four_is_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__test_four))
        testFour = self._driver.find_element(*self.__test_four)
        return testFour.is_displayed()


    def hit_testOne(self):
        tc_first = self._driver.find_element(*self.__test_one)
        tc_first.click()

    @property
    def text_of_testStepsOne(self):
        return self._driver.find_element(*self.__test_one).text



    @property
    def total_testSteps_verify(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_all_elements_located(self.__testSteps_div1))
        total_ts = self._driver.find_elements(*self.__testSteps_div1)
        return len(total_ts)

    def testSteps_one_collapse(self):
        ts_one = self._driver.find_element(*self.__collapse_btn)
        ts_one.click()


    @property
    def testSteps_are_gone(self):
        return not ec.visibility_of_all_elements_located(self.__testSteps_div1)


    def hit_testTwo(self):
        self._driver.find_element(*self.__test_two).click()

    @property
    def total_testSteps_verify_for_TC2(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_all_elements_located(self.__testSteps_div2))
        total_ts = self._driver.find_elements(*self.__testSteps_div2)
        return len(total_ts)


