import os
import unittest
from selenium import webdriver


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        # To Browser Chrome version 80
        cls.driver = webdriver.Chrome(
            executable_path=f'{dir_path}/webdrivers/chromedriver')
        cls.driver.get('http://localhost:3000/')

    def setUp(self):
        self.driver = self.__class__.driver

    def tearDown(self):
        # TODO: Esperar carregar a tela de home do perfil
        self.driver.find_element_by_id('logout').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_perfil_aluno(self):
        self.driver.find_element_by_id('login-input').send_keys('aluno1')
        self.driver.find_element_by_id('password').send_keys('123456')
        self.driver.find_element_by_id('submit-login').click()

    # def test_login_perfil_prof(self):
    #     self.driver.find_element_by_id('login-input').send_keys('prof')
    #     self.driver.find_element_by_id('password').send_keys('123456')
    #     self.driver.find_element_by_id('submit-login').click()

    # def test_login_perfil_editor(self):
    #     self.driver.find_element_by_id('login-input').send_keys('editor')
    #     self.driver.find_element_by_id('password').send_keys('123456')
    #     self.driver.find_element_by_id('submit-login').click()

    # def test_login_perfil_admin(self):
    #     self.driver.find_element_by_id('login-input').send_keys('admin')
    #     self.driver.find_element_by_id('password').send_keys('123456')
    #     self.driver.find_element_by_id('submit-login').click()


if __name__ == "__main__":
    unittest.main()
