#def usada na def user_search_news, user_comment_news, user_like_news
def search(news):
    found = False
    search = input('Pesquisa:')
    for autor, dicionario in news.items():
        for id_news, lista in dicionario.items():
            if search in lista[0]:
                found = True
                return found, autor, lista, id_news

    if not found:
        print('Nenhuma notícia encontrada!')
        return found, None, None, None


#def usada na def user_search_news e na def user_comment_news
def comment(news, autor, id_news):
    comentario = input('Comentário:')
    news[autor][id_news][2].append(comentario)
    print('\033[92mComentário adicionado\033[0m')


#essa def serve para o usuário buscar uma noticia
def user_search_news(news):
    x, autor, lista, id_news = search(news)
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


#essa def serve para o usuário comentar na notícia
def user_comment_news(news):
    comment_more = True
    while comment_more:
        x, autor, lista, id_news = search(news)
        if x:
            comment(news, autor, id_news)
        else:
            break

        other_comment = input('Deseja fazer mais um comentário? [sim/nao]')
        if other_comment == 'nao':
            comment_more = False


#essa def serve para o usuário curtir a notícia
def user_like_news(news):
    while True:
        x, autor, lista, id_news = search(news)
        if x:
            news[autor][id_news][3].append('❤️')
            print('\033[92mCurtida adicionada!\033[0m')

        other_like = input('Deseja curtir mais alguma noticia? [sim/nao]')
        if other_like == 'nao':
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
    email_user = perfis[usuario][2]
    author_user = input('Informe o nome de usuário do autor que você deseja adicionar aos favoritos.')
    if author_user in perfis and perfis[author_user][0] == '1':
        perfis[author_user][3].append(email_user)
        print('\033[92mAutor favoritado!\033[0m')
