from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class loginPage:
    __url = "https://login-app-iota.vercel.app"
    __username_textField = (By.ID, 'username_textbox')
    __password_textField = (By.ID, 'password_textbox')
    __login_button = (By.CSS_SELECTOR, "button[type='submit']")
    __error_lable_loginMsg = (By.XPATH, "//h1[normalize-space()='Contact List']")
    __login_error_msg = (By.XPATH, "//div[@class='text-center text-danger mb-2']")

    def __init__(self,driver:WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    @property
    def current_url(self):
        return self._driver.current_url

    def perform_login(self, username, password):
        pass_username = self._driver.find_element(*self.__username_textField)
        pass_password = self._driver.find_element(*self.__password_textField)
        press_loginBtn = self._driver.find_element(*self.__login_button)

        pass_username.send_keys(username)
        pass_password.send_keys(password)
        press_loginBtn.click()



    @property
    def _error_lable_text(self):
        pass_lable = self._driver.find_element(*self.__error_lable_loginMsg)
        login_txt = pass_lable.text
        return login_txt

    def is_error_lable_displayed(self)->bool:
        pass_lable = self._driver.find_element(*self.__error_lable_loginMsg)
        return pass_lable.is_displayed()

    @property
    def loginError_lable_text(self):
        login_error_txt = self._driver.find_element(*self.__login_error_msg)
        loginError_txt = login_error_txt.text
        return loginError_txt

    def is_loginError_lable_displayed(self)->bool:
        login_error_txt = self._driver.find_element(*self.__login_error_msg)
        return login_error_txt.is_displayed()






