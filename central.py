from register_adm import register_adm
from register_user import register_user
from login import login_adm_user
from menu_adm import *
from menu_user import *

everybody = {'adms': ['tiago2'], 'users': ['tiago1']}
passwords = {'password_adms': [12345], 'password_users': [12345]}
all_news = {1234: ['tiago é pego codando em php']}
body_news = {1234: 'qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjkl'}
data_news = {1234: ['tiagoeliashkss@gmail.com', '30/10/2022']}
emailUSER = []

while True:
    print(
        '___________MENU___________\n'
        '[1]Login\n'
        '[2]Cadastrar Administrador\n'
        '[3]Cadastrar usuário\n'
        '[0]Sair'
    )
    print('_'*26)
    choice = input()
    if choice == '1':
        tipo = login_adm_user(everybody, passwords)
        if tipo == 1:
            menu_adm(all_news, body_news, data_news)
        elif tipo == 2:
            menu_user(all_news, body_news, data_news, send_email)
        else:
            print('Usuário e senhas inválidos')

    elif choice == '2':
        register_adm(everybody, passwords)

    elif choice == '3':
        register_user(everybody, passwords, emailUSER)

    elif choice == '0':
        break

    else:
        print('Não existe essa opção.')
        break
