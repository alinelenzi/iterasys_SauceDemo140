#Bibliotecas
import pytest;
from selenium import webdriver;
from selenium.webdriver.common.by import By

#2. Classe(Opcional)
class Test_Produtos():

#2.1 Atributos
    url = "http://www.saucedemo.com"

#2.2 Funções e Métodos
    def setup_method(self, method):                                     # método de inicialização dos teste, fecundação podendo receber qq navegador
        self.driver = webdriver.Chrome();                               # instancia o objeto do selenium WebDriver como Chrome
        self.driver.implicitly_wait(10);                                # define o tempo de espera padrão por elementos em 1seg

    def teardown_method(self, method):                                  # método de finalização dos testes, morte
        # diferença entre quit (matou, só nascendo de novo)/ close (não morre, sai para almoço, volto logo)
        self.driver.quit();                                             # encerra/ destroi o objeto do Selenium WebDriver da memória

    def test_selecionar_produto(self):                                              # método teste
        self.driver.get(self.url)                                                   #abre navegador
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")     #colando o name
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")       #colando a senha