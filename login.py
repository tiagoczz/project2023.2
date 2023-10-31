#essa def está responsável pelo login dos usuários/adms
#tipo = 1(adm), tipo = 2(usuário) e tipo = 0(nada)
def login_adm_user(everybody, passwords):
    usuario = input('Usuário:')
    password = int(input('Senha:'))
    tipo = 0
    if usuario in everybody['adms'] and password in passwords['password_adms']:
        tipo = 1

    elif usuario in everybody['users'] and password in passwords['password_users']:
        tipo = 2

    return tipo
