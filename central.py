from register_adm import register_adm
from register_user import register_user
from login import login_adm_user
from menu_adm import *
from menu_user import *

id = [0]

users = {'tiago1': [12345, '1'], 'tiago2': [12345, '2']}
perfis = {'tiago1': ['1', 'Tiago Elias Abrantes Silva', 'tiagoeliashkss@gmail.com', ['tiagoeliassilva2005@gmail.com']], 'tiago2': ['2', 'Tiago Elias', 'tiagoeliassilva2005@gmail.com']}
news = {'tiago1': {id[0]: ['tiago é pego codando em php', 'tiago é pego em flagrante', ['não achei que ele fosse capaz disso'], ['❤️', '❤️'], '08/11/2023']},
        'elias1': {1: ['tiago é pego codando em javascript', 'pego em flagrante', ['hipocrita'], ['❤️', '❤️', '❤️', '❤️'], '08/11/2023']}}

my_news_rank = {}
geral_news_rank = {}
list_download_news = []

while True:
    print(
        '___________MENU___________\n'
        '[1]Login\n'
        '[2]Cadastrar Autor\n'
        '[3]Cadastrar Usuário\n'
        '[0]Sair'
    )
    print('_'*26)
    choice = input()
    if choice == '1':
        tipo, usuario = login_adm_user(users)
        if tipo == 1:
            menu_adm(news, id, usuario, my_news_rank, geral_news_rank, list_download_news, perfis)
        elif tipo == 2:
            menu_user(news, usuario, perfis)
        else:
            print('\033[91mUsuário e senhas inválidos!\033[0m')

    elif choice == '2':
        register_adm(users, perfis)

    elif choice == '3':
        register_user(users, perfis)

    elif choice == '0':
        break

    else:
        print('\033[91mOpção inválida!\033[0m')
        break
