import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class tasksPage:
    __url = "https://login-app-iota.vercel.app"
    __tasks_lnk = (By.LINK_TEXT, "Tasks")
    __heading_text_tasks = (By.CSS_SELECTOR, ".text-uppercase.text-center")
    __instructions = (By.XPATH, "//div[@class='border border-1 mt-2 px-4 py-2 d-flex flex-column rounded instruction']")
    __instruction_heading = (By.CSS_SELECTOR, "div[class='border border-1 mt-2 px-4 py-2 d-flex flex-column rounded instruction'] h5")

    __task_textBox = (By.ID, 'task-input')
    __task_addBtn = (By.CSS_SELECTOR, "button[class='btn btn-primary mb-2 ml-2 col-2']")
    __first_record = (By.XPATH, "//div[@class='border border-1 row m-2 p-1 rounded align-items-center bg-light']")

    __task_allIcons = (By.XPATH, "//div[@class='border border-1 row m-2 p-1 rounded align-items-center bg-light']//div[@class='col']//*[name()='svg']")
    __task_edit = (By.XPATH, "//*[name()='path' and contains(@d,'M880 836H1')]")
    __task_done = (By.XPATH, "//*[name()='path' and contains(@d,'M512 64C26')]")
    __task_delete = (By.XPATH, "//*[name()='path' and contains(@d,'M864 256H7')]")

    __save_btn = (By.CSS_SELECTOR, "button[class='btn btn-secondary mb-2 ml-2 col-2']")
    __the_updated_text = (By.XPATH, "//div[contains(text(),'My Second Task')]")

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

    def instruction_not_found(self):
        return ec.visibility_of_element_located(self.__instructions)

    def is_action_icons_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.visibility_of_all_elements_located(self.__task_allIcons))
        icons = self._driver.find_elements(*self.__task_allIcons)
        # if you do print instead return all three elements will be shown
        return icons


    def verify_edit(self):
        self._driver.find_element(*self.__task_edit).click()

    def click_save(self):
        self._driver.find_element(*self.__save_btn).click()


    def updated_text_is_displayed(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__the_updated_text))
        check_updated_task = self._driver.find_element(*self.__the_updated_text)
        return check_updated_task.is_displayed()

    def updated_text(self):
        updated_task_text = self._driver.find_element(*self.__the_updated_text).text
        return updated_task_text





















