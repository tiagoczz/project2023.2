adms = []
cpfADMs = []
emailADMs = []
passwordADMs = []
users = []
emailUSER = []
passwordUSER = []
all_news = {}
while True:
    print(
        '___________MENU___________\n'
        '[1]Cadastrar Administrador\n'
        '[2]Login\n'
        '[3]Cadastrar usuário\n'
        '[0]Sair'
    )
    print('_'*26)
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
                print('_'*26)
                print(
                    '[1]Inserir notícia\n'
                    '[2]Listar notícias\n'
                    '[3]Excluir notícia\n'
                    '[4]Editar notícia\n'
                    '[5]Buscar notícia\n'
                    '[6]Logout'
                )
                print('_'*26)
                choice = input()
                if choice == '1':
                    while True:
                        news_id = int(input('Crie um ID para a sua notícia:'))
                        for i in all_news.keys():
                            if i == news_id:
                                print('Você não pode informar o mesmo ID.')
                                news_id = int(input('Crie um outro ID:'))

                        news = input('Insira sua notícia:')
                        all_news[news_id] = [news]
                        yes_or_no = input('Ainda quer inserir notícias? sim/nao')
                        if yes_or_no == 'nao':
                            break

                elif choice == '2':
                    print('Essas são todas as notícias.')
                    for i in all_news.values():
                        no_quotes = str(i).strip("[]'")
                        print(no_quotes)
                    print('_'*26)
                    
                elif choice == '3':
                    while True:
                        remove_id = int(input('Informe o ID da notícia para remove-la:'))
                        if remove_id in all_news:
                            all_news.pop(remove_id)
                            print('Notícia removida.')
                            yes_or_no = input('Ainda quer remover uma noticia? sim/nao')
                            if yes_or_no == 'nao':
                                break
                        else:
                            print('ID inexistente!')
                            yes_or_no = input('Ainda quer remover uma noticia? sim/nao')
                            if yes_or_no == 'nao':
                                break

                elif choice == '4':
                    while True:
                        edit_id = int(input('Informe o ID da notícia que deseja editar:'))
                        if edit_id in all_news:
                            all_news.pop(edit_id)
                            question = input('Edite a notícia:')
                            all_news[edit_id] = [question]
                            yes_or_no = input('Deseja editar mais alguma coisa? sim/nao')
                            if yes_or_no == 'nao':
                                break
                        else:
                            print('Não existe nenhuma notícia relacionada a esse ID.')
                            yes_or_no = input('Deseja editar mais alguma coisa? sim/nao')
                            if yes_or_no == 'nao':
                                break

                elif choice == '5':
                    while True:
                        search_id = int(input('Informe o ID da notícia para busca-la:'))
                        if search_id in all_news:
                            search_no_quotes = str(search_id).strip("[]'")
                            print(all_news[search_id])
                            yes_or_no = input('Deseja continuar procurando? sim/nao')
                            if yes_or_no == 'nao':
                                break
                        else:
                            print('Digite algo válido')
                            yes_or_no = input('Deseja continuar procurando? sim/nao')
                            if yes_or_no == 'nao':
                                break

                elif choice == '6':
                    break
                else:
                    print('Não existe esse opção.')

        elif usuario in users and password in passwordUSER:
            logged = True
            while True:
                print('_'*26)
                print(
                    '[1]Buscar notícia\n'
                    '[2]Comentar notícia\n'
                    '[3]Curtir notícia\n'
                    '[4]Logout'
                )
                print('_' * 26)
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
