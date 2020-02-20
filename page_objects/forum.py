import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.ckeditor import Ckeditor


class Forum:
    def __init__(self, driver: webdriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait
        self.ckeditor = Ckeditor(self.driver, self.wait)

    def new_post(self):
        self._enter_valid_forum()

        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, 'button_new_post'))).click()

        time.sleep(1)
        self.ckeditor.post(css_seletor='#submit_post',
                           message='Criado pelo Selenium')

    def edit_post(self):
        self._enter_valid_forum()

        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'update_post'))).click()

        time.sleep(1)
        self.ckeditor.post(css_seletor='#submit_post',
                           message='Editado pelo Selenium')

    def response_post(self):
        self._enter_valid_forum()

        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'response_post'))).click()

        time.sleep(1)
        self.ckeditor.post(css_seletor='#submit_post',
                           message='Respondido pelo Selenium')

    def _enter_valid_forum(self):
        table = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'table.discussions tbody')))

        rows = table.find_elements_by_css_selector(
            'tr.lines:not(.period_ended)')

        for row in rows:
            situation = row.find_element_by_css_selector(
                'td[headers="situation"]').text
            if situation.strip() != 'Não iniciado':
                chosen_row = row
                break

        chosen_row.find_element_by_css_selector('a.link_content').click()
