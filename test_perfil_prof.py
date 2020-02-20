import os
import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver_factory import DriverFactory
from page_objects.login_page import LoginPage
from page_objects.mysolar_sidebar import MysolarSidebar
from page_objects.ckeditor import Ckeditor


class AlunoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverFactory.create_driver('chrome', visible=True)
        LoginPage(cls.driver).logar('prof', '123456')

    def setUp(self):
        self.browser = self.__class__.driver
        self.wait = WebDriverWait(self.browser, timeout=10)
        self.menu = MysolarSidebar(self.browser, self.wait)
        self.ckeditor = Ckeditor(self.browser, self.wait)

    def tearDown(self):
        self.browser.get('http://localhost:3000/home')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_cria_comentario_em_trabalho(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'td.center.link'))).click()

        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, 'Portfolio'))).click()

        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a.btn.participants'))).click()

        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'div.participants_box a.link_content:first-child'))).click()

        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable(
            (By.ID, 'new_comment'))).click()

        time.sleep(1)

        self.ckeditor.post('.save_comment')

        time.sleep(1)

        response_text = self.browser.find_element_by_id(
            'flash_message_span').text

        self.assertEqual(response_text, 'Comentário criado com sucesso')


if __name__ == "__main__":
    unittest.main()
