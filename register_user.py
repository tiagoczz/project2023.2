#tipo = 1(adm), tipo = 2(usuário) e tipo = 0(nada)
#def para cadastrar um usuario
def register_user(users, perfis):
    name = input('Nome:')
    email = input('Informe seu email:')
    while True:
        usuario = input('Crie um usuário:')
        # verifica se o usuario criado existe no dicionario users
        if usuario not in users:
            password = int(input('Crie uma senha:'))
            if len(str(password)) > 4:
            #cria uma nova chave(usuario) no dicionario users, e cria uma lista como valor contendo a senha e o tipo ='2'
                users[usuario] = [password, '2']
            #cria uma nova chave(usuario) no dicionario perfis, e cria uma lista como valor contendo tipo, o nome e o email
                perfis[usuario] = ['2', name, email]
                print('\033[92mCadastro concluído.\033[0m')
                break
            else:
                print('\033[91mSenha deve ter pelo menos 4 dígitos!\033[0m')
        else:
            print('\033[91mUsuário em uso. Tente outro!\033[0m')
