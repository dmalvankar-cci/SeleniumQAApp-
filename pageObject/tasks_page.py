from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class tasksPage:
    __url = "https://login-app-iota.vercel.app"
    __tasks_lnk = (By.LINK_TEXT, "Tasks")
    __heading_text_tasks = (By.CSS_SELECTOR, ".text-uppercase.text-center")
    __instructions = (By.XPATH, "//div[@class='border border-1 mt-2 px-4 py-2 d-flex flex-column rounded instruction']")

    __task_textBox = (By.ID, 'task-input')
    __task_addBtn = (By.CSS_SELECTOR, "button[class='btn btn-primary mb-2 ml-2 col-2']")
    __first_record = (By.XPATH, "//div[@class='border border-1 row m-2 p-1 rounded align-items-center bg-light']")


    def __init__(self,driver:WebDriver):
        self._driver = driver

    def hit_tasks(self):
        self._driver.find_element(*self.__tasks_lnk).click()


    @property
    def heading_text(self):
        head_txt = self._driver.find_element(*self.__heading_text_tasks).text
        return head_txt

    def is_heading_text_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__heading_text_tasks))
        head_txt = self._driver.find_element(*self.__heading_text_tasks)
        return head_txt.is_displayed()


    def is_instruction_text_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__instructions))
        instructions_txt = self._driver.find_element(*self.__instructions)
        return instructions_txt.is_displayed()

    def remove_placeholder(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__task_textBox))
        placeholder = self._driver.find_element(*self.__task_textBox)
        placeholder.clear()

    def click_add(self):
        self._driver.find_element(*self.__task_addBtn).click()

    def pass_task(self, task_name):
        textbox = self._driver.find_element(*self.__task_textBox)
        textbox.send_keys(task_name)

    def is_first_record_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__first_record))
        record_one = self._driver.find_element(*self.__first_record)
        return record_one.is_displayed()





