import time

import self
from selenium.webdriver.common.by import By

from Automation.Locators.locators import Home_locators


class Homeamazon:
    def __init__(self, driver):
        self.driver = driver

    def search_home(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, Home_locators.ALL).click()
        driver.find_element(By.XPATH, Home_locators.ECHO).click()
        # time.sleep(5)
