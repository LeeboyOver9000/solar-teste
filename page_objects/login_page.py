import time

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

    def deslogar(self, wait: WebDriverWait):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'logout'))).click()

    def cadastrar(self, cpf: str):
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, 'register-bt'))).click()

        # TODO: Casdastrar cpf usando o módulo Faker
