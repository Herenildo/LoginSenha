from controller import ControllerCadastro, ControllerLogin


while True:
    print("@@@@@@@@@@@@@@@@@@@@ [MENU] @@@@@@@@@@@@@@@@@@@@")
    decisao = int(input("Digite 1 para cadastrar\nDigite 2 para logar\nDigite 3 para sair:\n"))
    if decisao == 1:
        nome = input('Digite seu nome:\n')
        email = input('Digite seu email:\n')
        senha = input('Digite sua senha:\n')
        resultado = ControllerCadastro.cadastrar(nome, email, senha)

        if resultado == 2:
            print("Tamanho do nome digitado inválido")
        elif resultado == 3:
            print("Email maior que 200 caracteres")
        elif resultado == 4:
            print("Senha invalida")
        elif resultado == 5:
            print("Email já cadastrado")
        elif resultado == 6:
            print("Erro interno do sistema")
        elif resultado == 1:
            print("Cadastro realizado com sucesso")
    elif decisao == 2:
        email = input('Digite seu email:\n')
        senha = input('Digite sua senha:\n')
        resultado = ControllerLogin.login(email, senha)
        if  not resultado:
            print("Email ou senha inválidos")
        else:
            print(f"Login realizado com sucesso {resultado}")
    else:
        break
        