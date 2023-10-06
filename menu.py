nameADMs = []
cpfADMs = []
emailADMs = []
passwordADMs = []
nameUSER = []
emailUSER = []
passwordUSER = []
while True:
    print('1-Cadastrar ADM')
    print('2-Login')
    print('3-Cadastrar usuário')
    print('0-Sair')
    choice = input()
    if choice == '1':
        name1 = input('Nome:')
        nameADMs.append(name1)
        cpf = int(input('CPF:'))
        if len(str(cpf)) == 11:
            cpfADMs.append(cpf)
            email = input('Informe um e-mail:')
            emailADMs.append(email)
            password1 = int(input('Crie uma senha:'))
            if len(str(password1)) > 4:
                passwordADMs.append(password1)
                print('Cadastro concluído.')
            else:
                print('O cadastro não foi concluído.')
        else:
            print('CPF inválido.')
            break
    elif choice == '2':
        name = input('Nome:')
        password = int(input('Senha:'))
        logged = False
        for i in nameADMs:
            if nameADMs.count(name) == 1:
                for j in passwordADMs:
                    if passwordADMs.count(password) == 1:
                        logged = True
                        while True:
                            print('1-Inserir notícia')
                            print('2-Listar notícias')
                            print('3-Excluir notícia')
                            print('4-Editar notícia')
                            print('5-Buscar notícia')
                            print('6-Logout')
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
                                print('Aguarde futuras atualizações.')
                            else:
                                print('Não existe esse opção.')
                    else:
                        print('Senha incorreta.')
            else:
                print('Usuário incorreto.')
        if not logged:
            for i in nameUSER:
                if nameUSER.count(name) == 1:
                    for j in passwordUSER:
                        if passwordUSER.count(password) == 1:
                            logged = True
                            while True:
                                print('1-Buscar notícia')
                                print('2-Comentar notícia')
                                print('3-Curtir notícia')
                                choice = input()
                                if choice == '1':
                                    print('Aguarde futuras atualizações.')
                                elif choice == '2':
                                    print('Aguarde futuras atualizações.')
                                elif choice == '3':
                                    print('Aguarde futuras atualizações.')
                                else:
                                    print('Não existe essa opção.')
                        else:
                            print('Senha incorreta.')
                else:
                    print('Usuário incorreto.')
    elif choice == '3':
        name0 = input('Nome:')
        nameUSER.append(name0)
        email = input('Informe seu e-mail:')
        emailUSER.append(email)
        password0 = int(input('Crie uma senha:'))
        if len(str(password0)) > 4:
            passwordUSER.append(password0)
            print('Cadastro concluído:')
        else:
            print('O cadastro não foi concluído:')
    elif choice == '0':
        break
    else:
        print('Não existe essa opção.')
