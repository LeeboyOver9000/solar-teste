import time
import unittest

from pycpfcnpj import gen

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver_factory import DriverFactory
from page_objects.login_page import LoginPage


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
            self.login_page.deslogar()

    def test_faz_login_no_perfil_aluno(self):
        self.login_page.logar('aluno1', '123456')
        title_home = self.browser.title.split()[-1]
        self.assertEqual(title_home, 'Home')

    def test_novo_cadastro_de_aluno(self):
        self.login_page.cadastrar(gen.cpf())
        time.sleep(1)
        response_text = self.browser.find_element_by_id(
            'flash_message_span').text
        self.assertEqual(
            response_text, 'Bem vindo! Sua conta foi criada com sucesso.')

    def test_portal_navegacao_ufc(self):
        portal_ufc = self.login_page.navegar(
            'Portais', 'Universidade Federal do Ceará')
        self.assertEqual(portal_ufc, 'http://www.ufc.br/')

    def test_portal_navegacao_ufc_virtual(self):
        portal_virtual = self.login_page.navegar(
            'Portais', 'Instituto UFC Virtual')
        self.assertEqual(portal_virtual, 'http://portal.virtual.ufc.br/')


if __name__ == "__main__":
    unittest.main()
