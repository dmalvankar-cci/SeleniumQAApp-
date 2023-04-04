import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class contactPage:

    __contact_lnk = (By.LINK_TEXT, 'Contact')
    __contact_heading = (By.XPATH, "//div[@class='text-uppercase']")
    __table_contact = (By.XPATH, "//table[@class='table']")

    def __init__(self, driver: WebDriver):
        self._driver = driver


    def hit_contact(self):
        self._driver.find_element(*self.__contact_lnk).click()

    @property
    def contact_heading_text(self):
        head_txt = self._driver.find_element(*self.__contact_heading).text
        return head_txt

    def is_heading_text_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__contact_heading))
        head_txt = self._driver.find_element(*self.__contact_heading)
        return head_txt.is_displayed()

    def is_contact_table_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__table_contact))
        table = self._driver.find_element(*self.__table_contact)
        return table.is_displayed()