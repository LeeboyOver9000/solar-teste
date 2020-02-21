import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.login_page import LoginPage
from driver_factory import DriverFactory


class LoginPageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverFactory.create_driver('chrome', visible=True)
        cls.wait = WebDriverWait(cls.driver, timeout=10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.browser = self.__class__.driver
        self.wait = self.__class__.wait
        self.login_page = LoginPage(self.browser, self.wait)
        self.wait = WebDriverWait(self.browser, timeout=10)

    def tearDown(self):
        if self.browser.title.split()[-1] != 'Solar':
            self.login_page.deslogar(self.wait)

    # def test_faz_login_no_perfil_aluno(self):
    #     self.login_page.logar('aluno1', '123456')
    #     title_home = self.login_page.driver.title.split()[-1]
    #     self.assertEqual(title_home, 'Home')

    def test_novo_cadastro_de_aluno(self):
        self.login_page.cadastrar('72279108909')
        time.sleep(10)


if __name__ == "__main__":
    unittest.main()
