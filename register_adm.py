#tipo = 1(adm), tipo = 2(usuário) e tipo = 0(nada)
#def usada cadastrar um adm
def register_adm(users, perfis):
    name = input('Nome:')
    email = input('E-mail:')
    cpf = int(input('CPF:'))
    if len(str(cpf)) == 11:
        while True:
            usuario = input('Crie um usuário:')
            # verifica se o usuario criado existe no dicionario users
            if usuario not in users:
                password = int(input('Crie uma senha:'))
                if len(str(password)) >= 4:
                # cria uma nova chave(usuario) no dicionario users, e cria uma lista como valor contendo a senha e o tipo ='1'
                    users[usuario] = [password, '1']
                # cria uma nova chave(usuario) no dicionario perfis, e cria uma lista como valor contendo tipo, o nome,
                #o email e uma lista vazia que ira guardar os email dos usuarios que favoritaram esse autor
                    perfis[usuario] = ['1', name, email, []]
                    print('\033[92mCadastro Concluído.\033[0m')
                    break
                else:
                    print('\033[91mSenha deve ter pelo menos 4 dígitos!\033[0m')
            else:
                print('\033[91mUsuário em uso. Tente outro!\033[0m')
    else:
        print('\033[91mCPF inválido.\033[0m')
