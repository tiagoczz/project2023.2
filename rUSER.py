#def para buscar (usada na def user_search_news, user_comment_news, user_like_news)
def search(news):
    found = False
    search = input('Pesquisa:')
    #procura search no indice 0 (contem o titulo) da lista
    for autor, dicionario in news.items():
        for id_news, lista in dicionario.items():
            if search in lista[0]:
                #se encontrar found = True
                found = True

                return found, autor, lista, id_news

    #senao encontrar printa uma mensagem
    if not found:
        print('\033[91mNenhuma notícia encontrada!\033[0m')
        return found, None, None, None


#def para inserir comentario (usada na def user_search_news e na def user_comment_news)
def comment(news, autor, id_news):
    comentario = input('Comentário:')
    #insere na noticia do adm/autor o comentario
    news[autor][id_news][2].append(comentario)
    print('\033[92mComentário adicionado\033[0m')


#def para buscar uma noticia
def user_search_news(news):
    #recebe da def search found(x), autor da noticia, lista da noticia, e o id da noticia
    x, autor, lista, id_news = search(news)
    #se found for True
    if x:
        print(f'Publicado em {lista[4]}')
        print(f'Autor: {autor}')
        print(f'Título: {lista[0]}')
        print(f'Artigo: {lista[1]}')
        comentario = ', '.join(lista[2])
        print(f'Comentários: {comentario}')
        print(f'{len(lista[3])}❤️')
        add_comment = input('Deseja fazer um comentário? [sim/nao]')
        if add_comment == 'sim':
            comment(news, autor, id_news)


#def para comentar em uma noticia
def user_comment_news(news):
    comment_more = True
    while comment_more:
        #recebe da def search found(x), autor da noticia, lista da noticia, e o id da noticia
        x, autor, lista, id_news = search(news)
        # se found for True chama a def comment
        if x:
            comment(news, autor, id_news)
            other_comment = input('Deseja fazer mais um comentário? [sim/nao]')
            if other_comment == 'nao':
                comment_more = False

        else:
            comment_more = False


#def para curtir uma noticia
def user_like_news(news):
    while True:
        #recebe da def search found(x), autor da noticia, lista da noticia, e o id da noticia
        x, autor, lista, id_news = search(news)
        #se found for True insere um coração na noticia do adm/autor
        if x:
            news[autor][id_news][3].append('❤️')
            print('\033[92mCurtida adicionada!\033[0m')

            other_like = input('Deseja curtir mais alguma noticia? [sim/nao]')
            if other_like == 'nao':
                break
        else:
            break

#essa def serve para o usuário listar as notícias
def user_list_news(news):
    for x, y in news.items():
        for z in y:
            print(f'Autor: {x}')
            print(f'Publicado em {y[z][4]}')
            print(f'Título: {y[z][0]}')
            print(f'Artigo: {y[z][1]}')
            comentario = ', '.join(y[z][2])
            print(f'Comentários: {comentario}') if comentario else ''
            print(f'{len(y[z][3])}❤️')
            print('_' * 26)


#essa def serve para favoritar um autor/adm
def user_favorite_author(usuario, perfis):
    #guarda na variavel email_user o email do usuario
    email_user = perfis[usuario][2]
    author_user = input('Informe o nome de usuário do autor que você deseja adicionar aos favoritos:')
    #verifica se o nome de usuario do adm/autor existe no dicionario users e se o nome que foi informado é de um adm
    if author_user in perfis and perfis[author_user][0] == '1':
        # adiciona o email do usuario em uma lista
        perfis[author_user][3].append(email_user)
        print('\033[92mAutor favoritado!\033[0m')
    else:
        print('\033[91mAutor não foi encontrado!\033[0m')
