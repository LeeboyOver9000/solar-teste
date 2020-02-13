import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page_objects.login_page import LoginPage


class LoginPageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # options = Options()
        # options.headless = True
        # cls.driver = webdriver.Chrome(options=options)
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://localhost:3000/')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.login_page = LoginPage(self.__class__.driver)

    def tearDown(self):
        # TODO: Verificar se já está na tela de Login
        # self.login_page.deslogar()
        time.sleep(5)

    def test_faz_login_no_perfil_aluno(self):
        self.login_page.logar('aluno1', '123456')
        title_home = self.login_page.driver.title.split()[-1]
        self.assertEqual(title_home, 'Home')

    # def test_novo_cadastro_de_aluno(self):
    #     self.login_page.cadastrar('72279108909')
    #     # TODO


if __name__ == "__main__":
    unittest.main()
