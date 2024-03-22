Feature: Selecionar Produto

    Scenario: Selecionar produto "Sauce Labs Backpack"
        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuario standard_user e senha secret_sauce
        Then sou direcionado para pagina Home
    
    Scenario: Login com a senha invalida
        Given que entro no site Sauce Demo
        When preencho os campos de login com usuario standart_user e senha secret_sace
        Then exibe a mensagem de erro no login

    Scenario Outline: Login Negativo
        Given que entro no site Sauce Demo
        When preencho os campos de login com usuario <usuario> e senha <senha>
        Then exibe a <mensagem> de erro no login

        Examples:
        | id | usuario       | senha        | mensagem                                                                  |
        | 01 | standard_user | secret_sace  | Epic sadface: Username and password do not match any user in this service |
        | 02 | standard_user |              | Epic sadface: Password is required                                        |
        | 03 |               | secret_sauce | Epic sadface: Username is required                                        |
        | 04 | standard_use  | secret_sauce | Epic sadface: Username and password do not match any user in this service |
        | 05 | standard_use  |              | Epic sadface: Password is required                                        |
        | 06 |               |              | Epic sadface: Username is required                                        |
        | 07 | standard_use  | secret_sace  | Epic sadface: Username and password do not match any user in this service |
        | 08 |               | secret_sace  | Epic sadface: Username is required                                        |

    Scenario Outline: Login Negativo com IF
        Given que entro no site Sauce Demo
        When digito os campos de login com usuario <usuario> e senha <senha> com IF
        Then exibe a <mensagem> de erro no login

        Examples:
        | id | usuario       | senha        | mensagem                                                                  |
        | 01 | standard_user | secret_sace  | Epic sadface: Username and password do not match any user in this service |
        | 02 | standard_user | <branco>     | Epic sadface: Password is required                                        |
        | 03 | <branco>      | secret_sauce | Epic sadface: Username is required                                        |
        | 04 | standard_use  | secret_sauce | Epic sadface: Username and password do not match any user in this service |
        | 05 | standard_use  | <branco>     | Epic sadface: Password is required                                        |
        | 06 | <branco>      | <branco>     | Epic sadface: Username is required                                        |
        | 07 | standard_use  | secret_sace  | Epic sadface: Username and password do not match any user in this service |
        | 08 | <branco>      | secret_sace  | Epic sadface: Username is required                                        |