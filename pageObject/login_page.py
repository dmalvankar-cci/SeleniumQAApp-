from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class loginPage:
    __url = "https://login-app-iota.vercel.app"
    __username_textField = (By.ID, 'username_textbox')
    __password_textField = (By.ID, 'password_textbox')
    __login_button = (By.CSS_SELECTOR, "button[type='submit']")
    __dashboard_heading = (By.XPATH, "//h1[normalize-space()='Contact List']")
    __login_error_msg = (By.XPATH, "//div[@class='text-center text-danger mb-2']")
    __contact_lnk = (By.LINK_TEXT, 'Contact')

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
    def dashboarHeading_text(self):
        pass_lable = self._driver.find_element(*self.__dashboard_heading)
        login_txt = pass_lable.text
        return login_txt

    def is_dashboarHeading_text_displayed(self)->bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__dashboard_heading))
        pass_lable = self._driver.find_element(*self.__dashboard_heading)
        return pass_lable.is_displayed()

    @property
    def loginError_lable_text(self):
        login_error_txt = self._driver.find_element(*self.__login_error_msg)
        loginError_txt = login_error_txt.text
        return loginError_txt

    def is_loginError_lable_displayed(self)->bool:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__login_error_msg))
        login_error_txt = self._driver.find_element(*self.__login_error_msg)
        return login_error_txt.is_displayed()

    @property
    def contact_not_found(self):
        return not ec.visibility_of_element_located(self.__contact_lnk)






