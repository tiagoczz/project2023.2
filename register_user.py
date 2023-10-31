def register_user(everybody, passwords, emailUSER):
    name = input('Nome:')
    usuario = input('Crie um usuário:')
    if usuario in everybody['adms'] or usuario in everybody['users']:
        print('Usuário repetido, cadastre outro.')
    else:
        everybody['users'].append(usuario)
        email = input('Informe seu e-mail:')
        emailUSER.append(email)
        password = int(input('Crie uma senha:'))
        if len(str(password)) > 4:
            passwords['password_users'].append(password)
            print('Cadastro concluído.')
        else:
            print('A senha precisa possuir mais de 4 dígitos.')
