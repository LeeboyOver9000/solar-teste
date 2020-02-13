import os
import time
import unittest

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.login_page import LoginPage


class AlunoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # options = Options()
        # options.headless = True
        # cls.driver = webdriver.Chrome(options=options)
        cls.driver = webdriver.Chrome()
        LoginPage(cls.driver).logar('aluno1', '123456')

    def setUp(self):
        self.browser = self.__class__.driver
        self.wait = WebDriverWait(self.browser, timeout=10)

    def test_cria_comentario_em_trabalho(self):
        self.wait.until(ec.element_to_be_clickable(
            (By.CSS_SELECTOR, 'td.center.link'))).click()

        self.wait.until(ec.element_to_be_clickable(
            (By.LINK_TEXT, 'Portfolio'))).click()

        # TODO: Entrar nos participantes e criar o trabalho

        time.sleep(5)

    def tearDown(self):
        self.browser.get('http://localhost:3000/home')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()