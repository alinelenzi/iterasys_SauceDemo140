Feature: Selecionar Produto

    Scenario: Selecionar produto "Sauce Labs Backpack"
        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuario standart_user e senha secret_sauce
        Then sou direcionado para pagina Home
