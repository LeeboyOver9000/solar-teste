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
        cls.driver = DriverFactory.create_driver('chrome', visible=False)
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
        time.sleep(1)
        response_text = self.browser.find_element_by_id(
            'flash_message_span').text
        self.assertEqual(response_text, 'Login efetuado com sucesso.')

    def test_faz_login_no_perfil_professor(self):
        self.login_page.logar('prof', '123456')
        response_text = self.wait.until(
            EC.visibility_of_element_located((By.ID, 'flash_message_span'))).text
        self.assertEqual(response_text, 'Login efetuado com sucesso.')

    def test_faz_login_no_perfil_editor(self):
        self.login_page.logar('editor', '123456')
        response_text = self.wait.until(
            EC.visibility_of_element_located((By.ID, 'flash_message_span'))).text
        self.assertEqual(response_text, 'Login efetuado com sucesso.')

    def test_faz_login_no_perfil_admin(self):
        self.login_page.logar('admin', '123456')
        response_text = self.wait.until(
            EC.visibility_of_element_located((By.ID, 'flash_message_span'))).text
        self.assertEqual(response_text, 'Login efetuado com sucesso.')

    def test_novo_cadastro_de_aluno(self):
        self.login_page.cadastrar(gen.cpf())
        time.sleep(3)
        response_text = self.wait.until(
            EC.visibility_of_element_located((By.ID, 'flash_message_span'))).text
        self.assertEqual(
            response_text, 'Bem vindo! Sua conta foi criada com sucesso.')

    def test_navegacao_ufc(self):
        portal_ufc = self.login_page.navegar(
            'Portais', 'Universidade Federal do Ceará')
        self.assertEqual(portal_ufc, 'http://www.ufc.br/')

    def test_navegacao_ufc_virtual(self):
        portal_virtual = self.login_page.navegar(
            'Portais', 'Instituto UFC Virtual')
        self.assertEqual(portal_virtual, 'http://portal.virtual.ufc.br/')

    def test_navegacao_licenca(self):
        license_page = self.login_page.navegar(
            'Desenvolvimento', 'Termos de licença')
        self.assertEqual(
            license_page, 'https://github.com/wwagner33/solar/blob/master/GPLv3')

    def test_navegacao_equipe(self):
        readme_page = self.login_page.navegar(
            'Desenvolvimento', 'Equipe')
        self.assertEqual(
            readme_page, 'https://github.com/wwagner33/solar/blob/master/README')

    def test_navegacao_code(self):
        code_page = self.login_page.navegar(
            'Desenvolvimento', 'Código')
        self.assertEqual(
            code_page, 'https://github.com/wwagner33/solar')

    def test_navegacao_politica_privacidade(self):
        privacy_policy_page = self.login_page.navegar(
            'Política de privacidade')
        self.assertEqual(
            privacy_policy_page, 'http://localhost:3000/privacy_policy')

    def test_navegacao_app(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[href="/apps"]'))).click()

        time.sleep(1)
        app_page = self.browser.current_url
        self.assertEqual(app_page, 'http://localhost:3000/apps')
        self.browser.back()

    def test_navegacao_tutorials(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, 'Ajuda'))).click()

        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, 'Tutoriais'))).click()

        url = self.browser.current_url
        self.assertEqual(url, 'http://localhost:3000/tutorials_login')
        self.browser.back()

    def test_navegacao_videos_tutoriais(self):
        url = self.login_page.navegar('Ajuda', 'Vídeos tutoriais')
        self.assertEqual(url, 'http://localhost:3000/video_tutorials.html')

    def test_navegacao_faq(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, 'Ajuda'))).click()

        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, 'FAQ'))).click()

        url = self.browser.current_url
        self.assertEqual(url, 'http://localhost:3000/faq')
        self.browser.back()


if __name__ == "__main__":
    unittest.main()
