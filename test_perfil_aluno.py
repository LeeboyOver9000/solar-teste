import os
import time
import unittest
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver_factory import DriverFactory
from page_objects.login_page import LoginPage
from page_objects.mysolar_sidebar import MysolarSidebar
from page_objects.forum import Forum


class AlunoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverFactory.create_driver('chrome', visible=True)
        LoginPage(cls.driver).logar('aluno1', '123456')

    def setUp(self):
        self.browser = self.__class__.driver
        self.wait = WebDriverWait(self.browser, timeout=10)
        self.menu = MysolarSidebar(self.browser, self.wait)
        self.forum = Forum(self.browser, self.wait)

    def tearDown(self):
        self.browser.get('http://localhost:3000/home')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_abrir_aulas(self):
        self.menu.enter_menu('Aulas')

        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a.link_content.lesson'))).click()

        time.sleep(1)

        fancybox = self.browser.find_element_by_class_name('fancybox-iframe')
        self.browser.switch_to.frame(fancybox)

        time.sleep(1)

        self.wait.until(EC.visibility_of_element_located(
            (By.ID, 'module-selected'))).click()

        time.sleep(1)

        self.wait.until(EC.visibility_of_element_located(
            (By.ID, 'lmodule-options-dropdown'))).find_elements_by_tag_name('a')[-1].click()

        time.sleep(1)

        self.browser.switch_to.parent_frame()

    def test_download_material_de_apoio_quando_nao_existe_arquivo(self):
        self.menu.enter_menu('Material de Apoio')

        filename = self.browser.find_element_by_css_selector(
            '[headers="name_aulas"]').text

        link = self.browser.find_element_by_css_selector(
            '[headers="download_on_aulas"').find_element_by_tag_name('a')

        link.click()
        time.sleep(3)

        download_path = f'{Path.home()}/Downloads/{filename}'
        self.assertFalse(os.path.exists(download_path))

    def test_download_material_de_apoio_quando_arquivo_existe(self):
        self.menu.enter_menu('Material de Apoio')

        filename = self.browser.find_element_by_css_selector(
            '[headers="name_geral"]').text

        link = self.browser.find_element_by_css_selector(
            '[headers="download_on_geral"').find_element_by_tag_name('a')

        link.click()
        time.sleep(3)

        download_path = f'{Path.home()}/Downloads/{filename}'
        self.assertTrue(os.path.exists(download_path))

    def test_download_material_de_apoio_link(self):
        self.menu.enter_menu('Material de Apoio')

        original_window = self.browser.current_window_handle

        link = self.browser.find_element_by_css_selector(
            '[headers="download_on_links"').find_element_by_tag_name('a')

        link.click()
        time.sleep(3)

        self.wait.until(EC.number_of_windows_to_be(2))

        time.sleep(1)

        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
                self.browser.close()

        self.browser.switch_to.window(original_window)

    def test_cria_nova_postagem_no_forum(self):
        self.menu.enter_menu('Fórum')

        time.sleep(1)
        self.forum.make_new_post()

        time.sleep(1)
        response_text = self.browser.find_element_by_id(
            'flash_message_span').text

        self.assertEqual(response_text, 'Postagem criada com sucesso')

    def test_edita_postagem_do_forum(self):
        self.menu.enter_menu('Fórum')

        time.sleep(1)
        self.forum.edit_first_post()

        time.sleep(1)
        response_text = self.browser.find_element_by_id(
            'flash_message_span').text

        self.assertEqual(response_text, 'Postagem atualizada com sucesso')


if __name__ == "__main__":
    unittest.main()
