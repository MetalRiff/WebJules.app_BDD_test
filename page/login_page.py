import time

from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.XPATH, '//*[@placeholder = "Enter your email"]')
    PASSWORD = (By.XPATH, '//*[@placeholder = "Enter your password"]')
    BUTTON = (By.XPATH,'//*[@id="root"]/div/div[2]/form/div/div[3]/button/span[1]')
    ERROR = (By.XPATH, '//*[@id="client-snackbar"]/div/span')
    WRONG_EMAIL = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[1]/div/p')
    NO_PASSWORD = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[2]/div/p')


    def navigate_to_login_page(self):
        self.chrome.get('https://jules.app/sign-in')

    def insert_correct_email(self):
        self.chrome.find_element(*self.EMAIL).send_keys('stoican.adrian@yahoo.com')

    def insert_incorrect_email(self):
        self.chrome.find_element(*self.EMAIL).send_keys('incorect_email@test')

    def insert_correct_password(self):
        self.chrome.find_element(*self.PASSWORD).send_keys('P12345p!')

    def insert_incorrect_password(self):
        self.chrome.find_element(*self.PASSWORD).send_keys('P12345p!11')

    def insert_no_password(self):
        self.chrome.find_element(*self.PASSWORD).clear()

    def click_login_button(self):
        self.chrome.find_element(*self.BUTTON).click()


    def check_error_message(self):
        expected_error_message = 'Invalid email/password combination'
        actual_error_message = self.chrome.find_element(*self.ERROR).text
        time.sleep(3)
        assert expected_error_message == actual_error_message, "Error: Incorrect error message"

    def wrong_email_message(self):
        expected_message = 'Please enter a valid email address!'
        actual_message = self.chrome.find_element(*self.WRONG_EMAIL).text
        assert expected_message == actual_message, "Error: Incorrect error message"

    def no_password_message(self):
        expected_message = 'Please enter your password!'
        actual_message = self.chrome.find_element(*self.NO_PASSWORD).text
        time.sleep(3)
        assert expected_message == actual_message, "Error: wrong message"

    def click_logout_button(self):
        self.chrome.find_element(By.XPATH, '//*[@data-test-id="user-options-business-button"]').click()
        time.sleep(1)
        self.chrome.find_element(By.XPATH, '//*[@id="menu-list-grow"]/div[2]/li/span[1]').click()
        time.sleep(1)
        self.chrome.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]/span[1]').click()
        time.sleep(3)

        expected_url = 'https://jules.app/sign-in'
        actual_url = self.chrome.current_url

        assert expected_url == actual_url, "Error: wrong url"


