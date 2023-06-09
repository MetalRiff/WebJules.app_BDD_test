import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from base_page import BasePage


class SearchPage(BasePage):
    FILTER = (By.XPATH, '//*[@data-test-id="add-new-filter-button"]')
    RECORD = (By.XPATH, '//*[@id="menu-list-grow"]/div[1]/li')
    TYPE = (By.XPATH, '//*[@id="menu-list-grow"]/div[2]/li')
    CATEGORY = (By.XPATH, '//*[@id="menu-list-grow"]/div[3]/li')
    TAG = (By.XPATH, '//*[@id="menu-list-grow"]/div[4]/li')
    CONNECTION = (By.XPATH, '//*[@id="menu-list-grow"]/div[5]/li')
    USER_ACTIONS = (By.XPATH, '//*[@data-test-id="user-options-business-button"]')
    LOGOUT = (By.XPATH, '//*[@id="menu-list-grow"]/div[2]/li/span[1]')
    CONFIRM = (By.XPATH, '//*[@data-test-id="confirm-logout-button"]')
    MY_ITEMS = (By.XPATH, '//span[contains(text(),"My items")]')
    SEARCH = (By.XPATH, '//*[@class="MuiInputBase-input MuiInput-input"]')
    CONTEXT_MENU = (By.XPATH, '//*[@data-test-id="item-context-menu-button"]')
    DELETE_ITEM = (By.XPATH, '//span[contains(text(),"Delete Item")]')
    CONFIRM_DELETE_ITEM = (By.XPATH, '//*[@data-test-id="modal-card-delete-button"]')

    # method to access Filter button
    def click_filter_button(self):
        self.chrome.find_element(*self.FILTER).click()
        time.sleep(3)

    # method to select Record as filter
    def select_record_filter(self):
        self.chrome.find_element(*self.RECORD).click()
        time.sleep(3)

    # method to select Type as filter
    def select_type_filter(self):
        self.chrome.find_element(*self.TYPE).click()

    # method to select Category as filter
    def select_category_filter(self):
        self.chrome.find_element(*self.CATEGORY).click()

    # method to select Tag as filter
    def select_tag_filter(self):
        self.chrome.find_element(*self.TAG).click()

    # method to select Connection as filter
    def select_connection_filter(self):
        self.chrome.find_element(*self.CONNECTION).click()

    # method to delete recorded item
    def delete_item(self):
        self.chrome.find_element(*self.MY_ITEMS).click()
        time.sleep(1)
        self.chrome.find_element(*self.SEARCH).send_keys('A380', Keys.ENTER)
        time.sleep(1)
        self.chrome.find_element(*self.CONTEXT_MENU).click()
        time.sleep(1)
        self.chrome.find_element(*self.DELETE_ITEM).click()
        time.sleep(1)
        self.chrome.find_element(*self.CONFIRM_DELETE_ITEM).click()
        time.sleep(1)

    # method to check that we are on the Search page
    def check_current_page(self):
        expected = 'Search'
        actual = self.chrome.find_element(By.XPATH, '//*[@class="css-ffpnza"]/span').text
        assert expected == actual, "Error: wrong page"

    # method to Logout from Search page
    def click_logout_button(self):
        # load search page in browser
        self.chrome.get('https://jules.app/search/all')
        time.sleep(1)

        # access user actions menu
        self.chrome.find_element(*self.USER_ACTIONS).click()
        time.sleep(1)

        # logout
        self.chrome.find_element(*self.LOGOUT).click()
        time.sleep(1)

        # confirm logout and verify if the logout was done
        self.chrome.find_element(*self.CONFIRM).click()
        time.sleep(3)

        expected_url = 'https://jules.app/sign-in'
        actual_url = self.chrome.current_url

        assert expected_url == actual_url, "Error: wrong url"
