from rADM import *


def menu_adm(news, id, usuario, my_news_rank, geral_news_rank, list_download_news, perfis):
    while True:
        print('_' * 26)
        print(
            '[1]Inserir\n'
            '[2]Listar\n'
            '[3]Excluir\n'
            '[4]Editar\n'
            '[5]Buscar\n'
            '[6]Meu Ranking\n'
            '[7]Ranking geral\n'
            '[8]Baixar notícias\n'
            '[9]Logout'
        )
        print('_' * 26)
        try:
            choice = int(input())
            if choice == 1:
                adm_insert_news(news, id, usuario, perfis)

            elif choice == 2:
                adm_list_news(news, usuario)

            elif choice == 3:
                adm_remove_news(news, usuario)

            elif choice == 4:
                adm_edit_news(news, usuario)

            elif choice == 5:
                adm_search_news(news)

            elif choice == 6:
                adm_rank_news(news, usuario, my_news_rank)

            elif choice == 7:
                adm_geral_news_rank(news, geral_news_rank)

            elif choice == 8:
                adm_download_news(news, list_download_news, usuario)

            elif choice == 9:
                break

            else:
                print('\033[91mOpção inválida!\033[0m')

        except ValueError:
            print('\033[91mOpção inválida!\033[0m')
