from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.XPATH, '//*[@placeholder = "Enter your email"]')
    PASSWORD = (By.XPATH, '//*[@placeholder = "Enter your password"]')
    BUTTON = (By.XPATH,'//*[@data-test-id="login-button"]')



    def navigate_to_login_page(self):
        self.chrome.get('https://jules.app/sign-in')

    def insert_correct_email(self):
        self.chrome.find_element(*self.EMAIL).send_keys('stoican.adrian@yahoo.com')

    def insert_correct_password(self):
        self.chrome.find_element(*self.PASSWORD).send_keys('P12345p!')

