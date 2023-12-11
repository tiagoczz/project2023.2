#imports
from register_adm import register_adm
from register_user import register_user
from login import login_adm_user
from menu_adm import *
from menu_user import *

id = [0]
#dicionario users, com todos os usuarios incluindo adms
users = {'tiago1': [12345, '1'], 'tiago2': [12345, '2']}
#dicionario perfis, contendo informaçoes sobre os usuarios
perfis = {'tiago1': ['1', 'Tiago Elias Abrantes Silva', 'tiagoeliashkss@gmail.com', ['tiagoeliassilva2005@gmail.com']], 'tiago2': ['2', 'Tiago Elias', 'tiagoeliassilva2005@gmail.com']}
#dicionario com todas as noticias
news = {'tiago1': {id[0]: ['Botafogo perde a liderança do Brasileirão', 'Após perder a liderança o Botafogo vê o Palmeiras levantar a taça.', ['Acabou o gás do fogão'], ['❤️', '❤️'], '07/12/2023']},
        'elias1': {1: ['Saiu o trailer de GTA 6', '10 anos após o lançamento de GTA 5, foi revelado o trailer do GTA 6', ['sensacional o trailer'], ['❤️', '❤️', '❤️', '❤️'], '08/11/2023']}}

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
    try:
        choice = int(input())
        if choice == 1:
            # tipo = 1(adm), tipo = 2(usuário) e tipo = 0(nada)
            #chama a def login, e guarda em variaveis o tipo e o usuario
            tipo, usuario = login_adm_user(users)
            if tipo == 1:
                # se o tipo for igual a 1 chama a def do menu do adm
                menu_adm(news, id, usuario, my_news_rank, geral_news_rank, list_download_news, perfis)
            elif tipo == 2:
                #se o tipo for igual a 2 chama a def do menu do usuario
                menu_user(news, usuario, perfis)
            else:
                #se o tipo for igual a 0, informa que o usuario ou senha esta errado
                print('\033[91mUsuário ou senhas inválidos!\033[0m')

        elif choice == 2:
            #chama a def responsavel por cadastrar um adm
            register_adm(users, perfis)

        elif choice == 3:
            #chama a def responsavel por cadastrar um usuario
            register_user(users, perfis)

        elif choice == 0:
            break

        else:
            print('\033[91mOpção inválida!\033[0m')

    except ValueError:
        print('\033[91mOpção inválida!\033[0m')
