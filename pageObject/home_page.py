from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class homePage:
    __url = "https://login-app-iota.vercel.app"
    __heading_txt = (By.CSS_SELECTOR, ".text-center.text-primary.mb-3")
    __logout_lnk = (By.LINK_TEXT, "Logout")
    __home_lnk = (By.LINK_TEXT, "Home")
    __logo = (By.LINK_TEXT, "Selenium App")

    def __init__(self,driver:WebDriver):
        self._driver = driver

    def hit_home(self):
        self._driver.find_element(*self.__home_lnk).click()

    def hit_logo(self):
        self._driver.find_element(*self.__logo).click()


    @property
    def heading_text(self):
        head_txt = self._driver.find_element(*self.__heading_txt).text
        return head_txt

    def is_heading_text_displayed(self) -> bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__heading_txt))
        head_txt = self._driver.find_element(*self.__heading_txt)
        return head_txt.is_displayed()