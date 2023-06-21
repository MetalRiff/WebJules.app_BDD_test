import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from base_page import BasePage


class AddPage(BasePage):
    ADD = (By.XPATH, '//*[@data-test-id="add-flows-navigation-button"]')
    ITEM = (By.XPATH, '//*[@data-test-id="item-wizard-tile"]')
    MY_RECORD = (By.XPATH, '//*[@data-test-id="internal-item-tile"]')
    SEARCH = (By.XPATH, '//*[@placeholder="Start typing..." ]')
    CONTINUE_ADD = (By.XPATH, '//*[@data-test-id="add-item-type-step-continue-button"]')
    CONTINUE_RECORD = (By.XPATH,'//*[@data-test-id="record-type-step-continue-button"]')
    CONTINUE_NICKNAME = (By.XPATH, '//*[@data-test-id="nickname-step-continue-button"]')
    CONTINUE_NO_LOCATION = (By.XPATH, '//*[@data-test-id="location-step-continue-button"]')
    SKIP_AND_SAVE = (By.XPATH, '//*[@data-test-id="item-details-step-save-item-button"]')
    INPUT = (By.XPATH, '//*[@class="MuiInputBase-input MuiFilledInput-input"]')
    FINISH = (By.XPATH, '//span[contains(text(),"Finish")]')

    def access_add_page(self):
        self.chrome.find_element(*self.ADD).click()

    def add_item_to_records(self):
        self.chrome.find_element(*self.ITEM).click()
        self.chrome.find_element(*self.MY_RECORD).click()
        self.chrome.find_element(*self.SEARCH).send_keys('Airplane')
        self.chrome.find_element(*self.SEARCH).send_keys(Keys.ARROW_DOWN)
        self.chrome.find_element(*self.SEARCH).send_keys(Keys.ENTER)
        self.chrome.find_element(*self.CONTINUE_ADD).click()
        time.sleep(2)
        self.chrome.find_element(*self.CONTINUE_RECORD).click()
        self.chrome.find_element(*self.INPUT).send_keys('A380')
        time.sleep(2)
        self.chrome.find_element(*self.CONTINUE_NICKNAME).click()
        time.sleep(2)
        self.chrome.find_element(*self.CONTINUE_NO_LOCATION).click()
        time.sleep(2)
        self.chrome.find_element(*self.SKIP_AND_SAVE).click()
        time.sleep(2)
        self.chrome.find_element(*self.FINISH).click()
        time.sleep(2)
