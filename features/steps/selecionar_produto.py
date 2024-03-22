import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que entro no site Sauce Demo') #podia ter colocado a mesma frase só para ter um exemplo como faria com frases diferentes
@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    #Setup/inicialização
    context.driver = webdriver.Chrome()  # instanciar o objeto do Selenium WebDriver especializado para o Chrome
    context.driver.maximize_window()     # maximiazar a janela do navegador
    context.driver.implicitly_wait(10)       #esperar até 10 segundos por qualquer elemento
    #Passo em si
    context.driver.get("https://saucedemo.com") #abrir o navegador no endereço do site alvo

#Preencher com usuário e senha
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

#Preencher com usuário em branco e senha
@when(u'preencho os campos de login com usuario  e senha {senha}')
def step_impl(context, senha):
    #não preenche o usuário
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

#Preencher com usuário e mas senha em branco
@when(u'preencho os campos de login com usuario {usuario} e senha ')
def step_impl(context, usuario):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    #não preencho a senha
    context.driver.find_element(By.ID, "login-button").click()

#Sem preenche
@when(u'preencho os campos de login com usuario  e senha ')
def step_impl(context):
    #não preenche o usuário
    #não preencho a senha
    context.driver.find_element(By.ID, "login-button").click()

#Preencher com usuário e senha através da descisão (IF)
@when(u'digito os campos de login com usuario {usuario} e senha {senha} com IF')
def step_impl(context, usuario, senha):
    if (usuario != '<branco>'):
        context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    
    if senha !='<branco>':
        context.driver.find_element(By.ID, "password").send_keys(senha)
    

    context.driver.find_element(By.ID, "login-button").click()


@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"

#teardown/encerramento
    context.driver.quit()

#verifica a mensagem de erro
@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    #validar a mensagem de texto
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"

#verifica a mensagem para o Scenario Outline
@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
    #validar a mensagem de texto
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem

    #teardown/encerramento
    context.driver.quit()
