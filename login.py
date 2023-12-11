#essa def está responsável pelo login dos usuários/adms
#tipo = 1(adm), tipo = 2(usuário) e tipo = 0(nada)
def login_adm_user(users):
    tipo = 0
    usuario = input('Usuário:')
    password = int(input('Senha:'))
    #verifica se existe o usuario e a senha informados no dicionario users
    if usuario in users and password == users[usuario][0]:
        #se no dicionario users o indice 1 da lista for igual a 1, ele é um adm
        if users[usuario][1] == '1':
            tipo = 1
        #senao ele é um usuario
        else:
            tipo = 2

    #retorna o tipo e o nome de usuario
    return tipo, usuario
