from rADM import *


def menu_adm(all_news, body_news, data_news):
    while True:
        print('_' * 26)
        print(
            '[1]Inserir notícia\n'
            '[2]Listar notícias\n'
            '[3]Excluir notícia\n'
            '[4]Editar notícia\n'
            '[5]Buscar notícia\n'
            '[6]Logout'
        )
        print('_' * 26)
        choice = input()
        if choice == '1':
            adm_insert_news(all_news, body_news, data_news)

        elif choice == '2':
            adm_list_news(all_news, body_news)

        elif choice == '3':
            adm_remove_news(all_news, body_news)

        # RESOLVA ISSO WINICIUS
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
            adm_search_news(all_news, body_news)

        elif choice == '6':
            break

        else:
            print('Não existe esse opção.')
