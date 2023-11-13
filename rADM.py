#essa def serve para inserir noticias
def adm_insert_news(news, id, usuario):
    while True:
        title = input('Título:')
        article = input('Corpo da Notícia:')
        data = input('Insira a data de publicação da notícia no formato dia/mês/ano:')
        news_id = id[0] + 1
        id[0] = news_id
        if usuario in news:
            news[usuario][news_id] = [title, article, [], 'curtidas', data]
        else:
            news[usuario] = {news_id: [title, article, [], 'curtidas', data]}
        print('\033[92mNotícia adicionada!\033[0m')
        y = input('Deseja criar mais uma notícia? [sim/nao]')
        if y == 'nao':
            break


#essa def lista todas as notícias
def adm_list_news(news):
    for x, y in news.items():
        print(f'Autor: {x}')
        for z in y:
            print(f'Publicado em {y[z][4]}')
            print(f'Título: {y[z][0]}')
            print(f'Artigo: {y[z][1]}')
            comment = ', '. join(y[z][2])
            print(f'Comentários: {comment}') if comment else ''
            print(f'{len(y[z][3])}❤️')
            print('_'*26)


#essa def remove uma notícia
def adm_remove_news(news, usuario):
    while True:
        x = int(input(
            '[1]Excluir uma notícia\n'
            '[2]Excluir todas as notícias\n'
        ))
        if x == 1:
            id_to_remove = int(input('Informe o id da noticia para remove-la:'))
            if id_to_remove in news[usuario]:
                news[usuario].pop(id_to_remove)
                print('\033[92mNotícia removida!\033[0m')
                y = input('Deseja remover mais notícias? [sim/nao]')
                if y == 'nao':
                    break
            else:
                print('\033[91mID inexistente!\033[0m')
                break
        elif x == 2:
            news.pop(usuario)
            print('\033[92mTodas as notícia foram removidas!\033[0m')
            break
        else:
            print('\033[91mOpção inválida!\033[0m')


#essa def é para editar uma notícia
def adm_edit_news(news, usuario):
    while True:
        id_to_edit = int(input('Informe o id da noticia para edita-la:'))
        if id_to_edit in news[usuario]:
            junk = int(input(
                '[1]Editar título\n'
                '[2]Editar corpo\n'
                '[3]Editar toda a notícia\n'
            ))
            if junk == 1:
                new_title = input('Novo título:')
                news[usuario][id_to_edit][0] = new_title
                print('\033[92mNotícia salva!\033[0m')
                break
            elif junk == 2:
                new_article = input('Novo corpo:')
                news[usuario][id_to_edit][1] = new_article
                print('\033[92mNotícia salva!\033[0m')
                break
            elif junk == 3:
                new_title = input('Novo título:')
                news[usuario][id_to_edit][0] = new_title
                new_article = input('Novo corpo:')
                news[usuario][id_to_edit][1] = new_article
                print('\033[92mNotícia salva!\033[0m')
                break
            else:
                print('\033[91mID inexistente!\033[0m')
                break
        else:
            print('\033[91mID inexistente!\033[0m')


#essa def serve para buscar notícias
def adm_search_news(news, usuario):
    while True:
        id_to_search = int(input('Informe o ID da notícia para buscá-la:'))
        if usuario not in news or id_to_search not in news[usuario]:
            print('\033[91mID inexistente!\033[0m')
            continue
        else:
            print(f'\033[96mAutor: {usuario}\033[0m')
            print(f'Título: {news[usuario][id_to_search][0]}')
            print(f'Artigo: {news[usuario][id_to_search][1]}')
            print('_' * 26)

        break
