import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class contactPage:

    __contact_lnk = (By.LINK_TEXT, 'Contact')
    __contact_heading = (By.XPATH, "//div[@class='text-uppercase']")
    __table_contact = (By.XPATH, "//table[@class='table']")

    __plus_icon = (By.XPATH, "//div[@role='button']//*[name()='svg']")

    __form_elements = (By.CLASS_NAME, "form-control")

    __first_name = (By.XPATH, "(//input[@id='name_textbox'])[1]")
    __last_name = (By.XPATH, "(//input[@id='name_textbox'])[2]")
    __email = (By.ID, 'email_textbox')
    __phone = (By.ID, 'phone_textbox')
    __msg = (By.ID, 'message_textbox')

    __submit_btn = (By.CSS_SELECTOR, "button[type='submit']")

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
    def hit_plus_icon(self):
        self._driver.find_element(*self.__plus_icon).click()

    @property
    def is_form_fields_displayed(self) -> int:
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_all_elements_located(self.__form_elements))
        form_fields = self._driver.find_elements(*self.__form_elements)
        return len(form_fields)
    def is_submit_btn_displayed(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.presence_of_element_located(self.__submit_btn))
        submit_btn = self._driver.find_element(*self.__submit_btn)
        return submit_btn.is_displayed()
    def hit_submit_btn(self):
        self._driver.find_element(*self.__submit_btn).click()

    @property
    def verify_name_field_error(self):
        nameError = self._driver.find_element(*self.__first_name).get_attribute("validationMessage")
        return nameError


    def pass_data_in_fields(self, fname, lname, email, phone, msg):
       Fname =  self._driver.find_element(*self.__first_name)
       Lname =  self._driver.find_element(*self.__last_name)
       Email = self._driver.find_element(*self.__email)
       Phone = self._driver.find_element(*self.__phone)
       textArea = self._driver.find_element(*self.__msg)

       Fname.send_keys(fname)
       Lname.send_keys(lname)
       Email.send_keys(email)
       Phone.send_keys(phone)
       textArea.send_keys(msg)


    @property
    def verify_email_field_error(self):
        emailError = self._driver.find_element(*self.__email).get_attribute("validationMessage")
        return emailError