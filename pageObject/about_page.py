from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class aboutPage:
    __url = "https://login-app-iota.vercel.app"
    __heading_txt = (By.CSS_SELECTOR, ".text-center.text-primary")
    __logout_lnk = (By.LINK_TEXT, "Logout")
    __about_lnk = (By.LINK_TEXT, "About")
    def __init__(self,driver:WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    @property
    def current_url(self):
        return self._driver.current_url

    def about_action(self):
        self._driver.find_element(*self.__about_lnk).click()

    def logout_action(self):
        self._driver.find_element(*self.__logout_lnk).click()

    @property
    def heading_text(self):
        head_txt = self._driver.find_element(*self.__heading_txt).text
        return head_txt

    def is_heading_text_displayed(self) -> bool:
        head_txt = self._driver.find_element(*self.__heading_txt)
        return head_txt.is_displayed()