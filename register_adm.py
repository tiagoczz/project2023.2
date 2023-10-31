def register_adm(everybody, passwords):
    name = input('Nome:')
    usuario = input('Crie um usuário:')
    if usuario in everybody['adms'] or usuario in everybody['users']:
        print('Usuario existente, cadastre outro')
    else:
        everybody['adms'].append(usuario)
        cpf = int(input('CPF:'))
        if len(str(cpf)) == 11:
            password = int(input('Crie uma senha:'))
            if len(str(password)) > 4:
                passwords['password_adms'].append(password)
                print('Cadastro concluído.')
            else:
                print('A senha precisa possuir mais de 4 dígitos.')
        else:
            print('CPF inválido.')
