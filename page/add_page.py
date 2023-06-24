import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddPage(BasePage):
    ADD = (By.XPATH, '//*[@data-test-id="add-flows-navigation-button"]')
    ITEM = (By.XPATH, '//*[@data-test-id="item-wizard-tile"]')
    MY_RECORD = (By.XPATH, '//*[@data-test-id="internal-item-tile"]')
    SEARCH = (By.XPATH, '//*[@placeholder="Start typing..." ]')
    CONTINUE_ADD = (By.XPATH, '//*[@data-test-id="add-item-type-step-continue-button"]')
    CONTINUE_RECORD = (By.XPATH, '//*[@data-test-id="record-type-step-continue-button"]')
    CONTINUE_NICKNAME = (By.XPATH, '//*[@data-test-id="nickname-step-continue-button"]')
    CONTINUE_NO_LOCATION = (By.XPATH, '//*[@data-test-id="location-step-continue-button"]')
    SKIP_AND_SAVE = (By.XPATH, '//*[@data-test-id="item-details-step-save-item-button"]')
    INPUT = (By.XPATH, '//*[@class="MuiInputBase-input MuiFilledInput-input"]')
    FINISH = (By.XPATH, '//span[contains(text(),"Finish")]')
    CLOSE_ADD_ITEM = (By.XPATH, '//span[contains(text(),"CLOSE")]')

    # method to access Add page
    def access_add_page(self):
        self.chrome.find_element(*self.ADD).click()

    # method to abort add via close
    def close_add(self):
        close = self.chrome.find_element(*self.CLOSE_ADD_ITEM)
        WebDriverWait(self.chrome,1).until(EC.element_to_be_clickable(close))
        close.click()

    # method to add Airplane items from a list
    def add_item_to_records(self):
        airplane_list = ['A380', 'A220', 'A330']

        for avion in airplane_list:
            self.chrome.find_element(*self.ADD).click()
            self.chrome.find_element(*self.ITEM).click()
            self.chrome.find_element(*self.MY_RECORD).click()
            self.chrome.find_element(*self.SEARCH).send_keys('Airplane')
            self.chrome.find_element(*self.SEARCH).send_keys(Keys.ARROW_DOWN)
            self.chrome.find_element(*self.SEARCH).send_keys(Keys.ENTER)
            self.chrome.find_element(*self.CONTINUE_ADD).click()
            time.sleep(2)
            self.chrome.find_element(*self.CONTINUE_RECORD).click()
            self.chrome.find_element(*self.INPUT).send_keys(avion)
            time.sleep(2)
            self.chrome.find_element(*self.CONTINUE_NICKNAME).click()
            time.sleep(2)
            self.chrome.find_element(*self.CONTINUE_NO_LOCATION).click()
            time.sleep(2)
            self.chrome.find_element(*self.SKIP_AND_SAVE).click()
            time.sleep(2)
            self.chrome.find_element(*self.FINISH).click()
            time.sleep(1)
