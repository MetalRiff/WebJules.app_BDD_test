import time
from selenium.webdriver.common.by import By
from base_page import BasePage


class SearchPage(BasePage):
    FILTER = (By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div[3]/div[2]/div[1]/div/button')
    RECORD = (By.XPATH, '//*[@id="menu-list-grow"]/div[1]/li')
    TYPE = (By.XPATH, '//*[@id="menu-list-grow"]/div[2]/li')
    CATEGORY = (By.XPATH, '//*[@id="menu-list-grow"]/div[3]/li')
    TAG = (By.XPATH, '//*[@id="menu-list-grow"]/div[4]/li')
    CONNECTION = (By.XPATH, '//*[@id="menu-list-grow"]/div[5]/li')



    def click_filter_button(self):
        self.chrome.find_element(*self.FILTER).click()

    def select_record_filter(self):
        self.chrome.find_element(*self.RECORD).click()

    def select_type_filter(self):
        self.chrome.find_element(*self.TYPE).click()

    def select_category_filter(self):
        self.chrome.find_element(*self.CATEGORY).click()

    def select_tag_filter(self):
        self.chrome.find_element(*self.TAG).click()

    def select_connection_filter(self):
        self.chrome.find_element(*self.CONNECTION).click()

    def check_current_page(self):

        expected = 'Search'
        actual = self.chrome.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[2]/div[1]/div[2]/span').text
        assert expected == actual, "Error: wrong page"

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
