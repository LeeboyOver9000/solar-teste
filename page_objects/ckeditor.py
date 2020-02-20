import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Ckeditor:
    def __init__(self, driver: webdriver, wait: WebDriverWait):
        self.browser = driver
        self.wait = wait

    def post(self, css_seletor: str, message: str = 'Enviado usando o Selenium'):
        time.sleep(1)
        iframe = self.browser.switch_to.active_element
        self.browser.switch_to.frame(iframe)

        ckeditor = self.browser.find_element_by_css_selector(
            '[contenteditable="true"]')

        ckeditor.clear()
        ckeditor.send_keys(message)

        self.browser.switch_to.parent_frame()
        self.browser.find_element_by_css_selector(css_seletor).click()
