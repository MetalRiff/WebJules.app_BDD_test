import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Browser:

    # instantiem un browser
    # sa accesam site-ul pe care il testam
    # sa maximizez fereastra
    # optional: sa adaugam un implicit wait

    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.implicitly_wait(5)


    def close(self):
        self.chrome.quit()