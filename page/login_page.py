import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.XPATH, '//*[@placeholder = "Enter your email"]')
    PASSWORD = (By.XPATH, '//*[@placeholder = "Enter your password"]')
    BUTTON = (By.XPATH, '//*[@class="MuiButton-label"]')
    ERROR = (By.XPATH, '//*[@id="client-snackbar"]/div/span')
    WRONG_EMAIL = (By.XPATH, '//p[contains(text(),"Please enter a valid email address!")]')
    NO_PASSWORD = (By.XPATH, '//p[contains(text(),"Please enter your password!")]')

    def navigate_to_login_page(self):
        self.chrome.get('https://jules.app/sign-in')

    def insert_email(self, email):
        self.chrome.find_element(*self.EMAIL).send_keys(email)

    def insert_password(self, password):
        self.chrome.find_element(*self.PASSWORD).send_keys(password)

    def insert_no_password(self):
        self.chrome.find_element(*self.PASSWORD).send_keys('1')
        time.sleep(1)
        self.chrome.find_element(*self.PASSWORD).send_keys(Keys.BACK_SPACE)

    def click_login_button(self):
        self.chrome.find_element(*self.BUTTON).click()

    def check_error_message(self):
        expected_error_message = 'Invalid email/password combination'
        actual_message = self.chrome.find_element(*self.ERROR).text
        time.sleep(2)
        assert expected_error_message == actual_message, "Error: Incorrect error message"

    def wrong_email_message(self):
        expected_message = 'Please enter a valid email address!'
        actual_message = self.chrome.find_element(*self.WRONG_EMAIL).text
        time.sleep(3)
        assert expected_message == actual_message, "Error: Incorrect error message"

    def no_password_message(self):
        expected_message = 'Please enter your password!'
        actual_message = self.chrome.find_element(*self.NO_PASSWORD).text
        time.sleep(3)
        assert expected_message == actual_message, "Error: wrong message"
