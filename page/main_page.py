import time

from base_page import BasePage


class MainPage(BasePage):

    def check_current_url(self):

        expected_url = 'https://jules.app/search/all'
        actual_url = self.chrome.current_url
        time.sleep(3)
        assert expected_url != actual_url, "Error: invalid URL"
