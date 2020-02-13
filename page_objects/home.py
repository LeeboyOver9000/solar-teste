from selenium import webdriver


class Home:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def navegar(self, css_seletor: str):
        pass

    def buscar(self, disciplina: str):
        pass
