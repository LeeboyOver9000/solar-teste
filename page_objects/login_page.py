import time

from faker import Faker

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver: webdriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000/')

    def logar(self, login: str, senha: str):
        self.driver.find_element_by_id('login-input').send_keys(login)
        self.driver.find_element_by_id('password').send_keys(senha)
        self.driver.find_element_by_id('submit-login').click()

    def deslogar(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'logout'))).click()
        time.sleep(1)

    def navegar(self, menu_name: str, link_name: str):
        self.wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, menu_name))).click()

        time.sleep(1)
        original_window = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, link_name))).click()

        time.sleep(1)
        self.wait.until(EC.number_of_windows_to_be(2))

        time.sleep(1)
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                site_open = self.driver.current_url
                self.driver.close()

        self.driver.switch_to.window(original_window)
        return site_open

    def cadastrar(self, cpf: str):
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, 'register-bt'))).click()

        time.sleep(1)
        self.driver.find_element_by_id('cpf-register').send_keys(cpf)
        self.driver.find_element_by_id('submit-cpf').click()

        time.sleep(1)
        fake = Faker('pt_BR')

        self.driver.find_element_by_id('user_name').send_keys(fake.name())
        self.driver.find_element_by_id('next_1').click()

        time.sleep(1)
        self.driver.find_element_by_id(
            'user_nick').send_keys(fake.first_name())
        username = '_'.join(fake.last_name().split())
        self.driver.find_element_by_id(
            'user_username').send_keys(f'Selenium_{username}')
        self.driver.find_element_by_id(
            'user_password').send_keys('123456')
        self.driver.find_element_by_id(
            'user_password_confirmation').send_keys('123456')

        email = fake.email()
        self.driver.find_element_by_id('user_email').send_keys(email)
        self.driver.find_element_by_id(
            'user_email_confirmation').send_keys(email)

        next_buttons = self.driver.find_elements_by_css_selector('a.btn.next')
        next_buttons[0].click()

        time.sleep(1)
        next_buttons[1].click()

        time.sleep(1)
        self.driver.find_element_by_id('complete').click()
