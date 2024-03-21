import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    #Setup/inicialização
    context.driver = webdriver.Chrome()  # instanciar o objeto do Selenium WebDriver especializado para o Chrome
    context.driver.maximize_window()     # maximiazar a janela do navegador
    context.driver.implicitly_wait       #esperar até 10 segundos por qualquer elemento
    #Passo em si
    context.driver.get("https://saucedemo.com") #abrir o navegador no endereço do site alvo

@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELETOR, ".title").text == "Prodcts"

#teardown/encerramento
    context.driver.quit()
