adms = []
cpfADMs = []
emailADMs = []
passwordADMs = []
users = []
emailUSER = []
passwordUSER = []
while True:
    print('-----------MENU-----------')
    print('[1]Cadastrar Administrador')
    print('[2]Login')
    print('[3]Cadastrar usuário')
    print('[0]Sair')
    print('-'*26)
    choice = input()
    if choice == '1':
        name = input('Nome:')
        usuario = input('Crie um usuário:')
        if usuario in adms or usuario in users:
            print('Usuario existente, cadastre outro')
        else:
            adms.append(usuario)
            cpf = int(input('CPF:'))
            if len(str(cpf)) == 11:
                cpfADMs.append(cpf)
                email = input('Informe um e-mail:')
                emailADMs.append(email)
                password = int(input('Crie uma senha:'))
                if len(str(password)) > 4:
                    passwordADMs.append(password)
                    print('Cadastro concluído.')
                else:
                    print('A senha precisa possuir mais de 4 dígitos.')
            else:
                print('CPF inválido.')
    elif choice == '2':
        usuario = input('Usuário:')
        password = int(input('Senha:'))
        logged = False
        if usuario in adms and password in passwordADMs:
            logged = True
            while True:

                print(
                    '[1]Inserir notícia\n'
                    '[2]Listar notícias\n'
                    '[3]Excluir notícia\n'
                    '[4]Editar notícia\n'
                    '[5]Buscar notícia\n'
                    '[6]Logout\n'
                )
                choice = input()
                if choice == '1':
                    print('Aguarde futuras atualizações.')
                elif choice == '2':
                    print('Aguarde futuras atualizações.')
                elif choice == '3':
                    print('Aguarde futuras atualizações.')
                elif choice == '4':
                    print('Aguarde futuras atualizações.')
                elif choice == '5':
                    print('Aguarde futuras atualizações.')
                elif choice == '6':
                    break
                else:
                    print('Não existe esse opção.')

        if usuario in users and password in passwordUSER:
            logged = True
            while True:
                print(
                    '[1]Buscar notícia\n'
                    '[2]Comentar notícia\n'
                    '[3]Curtir notícia\n'
                    '[4]Logout\n'
                )
                choice = input()
                if choice == '1':
                    print('Aguarde futuras atualizações.')
                elif choice == '2':
                    print('Aguarde futuras atualizações.')
                elif choice == '3':
                    print('Aguarde futuras atualizações.')
                elif choice == '4':
                    break
                else:
                    print('Não existe essa opção.')

        else:
            print('Usuário ou senha incorretos')
    elif choice == '3':
        name = input('Nome:')
        usuario = input('Crie um usuário:')
        if usuario in adms or usuario in users:
            print('Usuário repetido, cadastre outro.')
        else:
            users.append(usuario)
            email = input('Informe seu e-mail:')
            emailUSER.append(email)
            password = int(input('Crie uma senha:'))
            if len(str(password)) > 4:
                passwordUSER.append(password)
                print('Cadastro concluído:')
            else:
                print('A senha precisa possuir mais de 4 dígitos.')
    elif choice == '0':
        break
    else:
        print('Não existe essa opção.')
        break
