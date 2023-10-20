everybody = {'adms': ['tiago2'], 'users': ['tiago1']}
passwords = {'password_adms': [12345], 'password_users': [12345]}
all_news = {1234: ['tiago é pego codando em php']}
#tava pensando em deixar tudo na mesma lista  all_news = {1234: ['tiago é pego codando em php', 'comentário', 'curtidas']}
emailADMs = []
emailUSER = []
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
        if usuario in everybody['adms'] or usuario in everybody['users']:
            print('Usuario existente, cadastre outro')
        else:
            everybody['adms'].append(usuario)
            cpf = int(input('CPF:'))
            if len(str(cpf)) == 11:
                email = input('Informe um e-mail:')
                emailADMs.append(email)
                password = int(input('Crie uma senha:'))
                if len(str(password)) > 4:
                    passwords['password_adms'].append(password)
                    print('Cadastro concluído.')
                else:
                    print('A senha precisa possuir mais de 4 dígitos.')
            else:
                print('CPF inválido.')

    elif choice == '2':
        usuario = input('Usuário:')
        password = int(input('Senha:'))
        logged = False
        if usuario in everybody['adms'] and password in passwords['password_adms']:
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
                            print(all_news[search_id][0])
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

        elif usuario in everybody['users'] and password in passwords['password_users']:
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
                    while True:
                        search_id = int(input('Informe o ID da notícia para busca-la:'))
                        if search_id in all_news:
                            print(all_news[search_id][0])
                            yes_or_no = input('Deseja continuar procurando? sim/nao')
                            if yes_or_no == 'nao':
                                break
                        else:
                            print('Não existe nenhuma notícia com esse ID.')
                            yes_or_no = input('Deseja continuar procurando? sim/nao')
                            if yes_or_no == 'nao':
                                break

                elif choice == '2':
                    while True:
                        comment_id = int(input('Informe o ID da notícia para comentar:'))
                        if comment_id in all_news:
                            comment = input('Comentário:')
                            all_news[comment_id].append(comment)
                            yes_or_no = input('Deseja continuar comentando? sim/nao')
                            if yes_or_no == 'nao':
                                break
                        else:
                            print('Não existe nenhuma notícia com esse ID.')
                            yes_or_no = input('Ainda quer comentar? sim/nao')
                            if yes_or_no == 'nao':
                                break

                elif choice == '3':
                    while True:
                        like_id = int(input('Informe o ID da notícia para comentar:'))
                        if like_id in all_news:
                            like = input('Para curtir digite 1:')
                            if like == '1':
                                all_news[like_id].append(like)
                                yes_or_no = input('Deseja curtir mais alguma notícia? sim/nao')
                                if yes_or_no == 'nao':
                                    break
                        else:
                            print('Não existe nenhuma notícia com esse ID.')
                            yes_or_no = input('Deseja curtir mais alguma notícia? sim/nao')
                            if yes_or_no == 'nao':
                                break

                elif choice == '4':
                    break

                else:
                    print('Não existe essa opção.')

        else:
            print('Usuário ou senha incorretos')

    elif choice == '3':
        name = input('Nome:')
        usuario = input('Crie um usuário:')
        if usuario in everybody['adms'] or usuario in everybody['users']:
            print('Usuário repetido, cadastre outro.')
        else:
            everybody['users'].append(usuario)
            email = input('Informe seu e-mail:')
            emailUSER.append(email)
            password = int(input('Crie uma senha:'))
            if len(str(password)) > 4:
                passwords['password_users'].append(password)
                print('Cadastro concluído.')
            else:
                print('A senha precisa possuir mais de 4 dígitos.')

    elif choice == '0':
        break

    else:
        print('Não existe essa opção.')
        break
