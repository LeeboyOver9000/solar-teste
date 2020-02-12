import os
import time
import unittest
from selenium import webdriver


class LoginPage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def logar(self, login: str, senha: str):
        self.driver.find_element_by_id('login-input').send_keys(login)
        self.driver.find_element_by_id('password').send_keys(senha)
        self.driver.find_element_by_id('submit-login').click()

    def cadastrar(self, cpf: str):
        pass


class AlunoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        # To Browser Chrome version 80
        cls.driver = webdriver.Chrome(
            executable_path=f'{dir_path}/webdrivers/chromedriver')
        cls.driver.get('http://localhost:3000/')

    def setUp(self):
        self.login_page = LoginPage(self.__class__.driver)

    def tearDown(self):
        # TODO: Limpar todos os campos de formulários
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_faz_login_no_perfil_aluno(self):
        self.login_page.logar('aluno1', '123456')


if __name__ == "__main__":
    unittest.main()
