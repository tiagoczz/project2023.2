from rUSER import*


def menu_user(all_news, body_news, data_news, send_email):
    while True:
        print('_' * 26)
        print(
            '[1]Buscar\n'
            '[2]Comentar\n'
            '[3]Curtir\n'
            '[4]Listar\n'
            '[5]Logout'
        )
        print('_' * 26)
        choice = input()
        if choice == '1':
            user_search_news(all_news, body_news, data_news, send_email)

        elif choice == '2':
            user_comment_news(all_news, data_news, send_email)

        elif choice == '3':
            user_like_news(all_news)

        elif choice == '4':
            user_list_news(all_news, body_news)

        elif choice == '5':
            break

        else:
            print('Opção inválida.')
