from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get('http://localhost:3000/')

    def logar(self, login: str, senha: str):
        self.driver.find_element_by_id('login-input').send_keys(login)
        self.driver.find_element_by_id('password').send_keys(senha)
        self.driver.find_element_by_id('submit-login').click()

    def deslogar(self):
        WebDriverWait(self.driver, timeout=5).until(
            ec.element_to_be_clickable((By.ID, 'logout'))).click()

    def cadastrar(self, cpf: str):
        pass
