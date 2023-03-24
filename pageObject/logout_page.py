from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class logoutPage:
    __url = "https://login-app-iota.vercel.app"
    __logout_lnk = (By.LINK_TEXT, "Logout")

    def __init__(self,driver:WebDriver):
        self._driver = driver

    def logout_action(self):
        self._driver.find_element(*self.__logout_lnk).click()






