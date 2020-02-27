import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MysolarSidebar:
    def __init__(self, driver: webdriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    def enter_menu(self, menu_name: str):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'td.center.link'))).click()
        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, f'{menu_name}'))).click()
        time.sleep(1)
