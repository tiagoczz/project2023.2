import smtplib
import email.message


#essa def serve para enviar o email
def send_email(title, usuario, perfis):
    for i, j in perfis.items():
        if j[0] == '1':
            for k in j[3]:
                msg = email.message.Message()
                msg['Subject'] = f'{usuario} postou uma nova notícia!'
                msg['From'] = 'jamesbot.ifpb@gmail.com'
                msg['To'] = k
                password = 'lied uthj dsde rdax'
                msg.add_header('Content-type', 'txt/html')
                msg.set_payload(title)

                s = smtplib.SMTP('smtp.gmail.com: 587')
                s.starttls()

                s.login(msg['From'], password)
                s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))


#essa def serve para inserir noticias
def adm_insert_news(news, id, usuario, perfis):
    while True:
        title = input('Título:')
        article = input('Corpo da Notícia:')
        data = input('Insira a data de publicação da notícia no formato dia/mês/ano:')
        news_id = id[0] + 1
        id[0] = news_id

        if usuario in news:
            news[usuario][news_id] = [title, article, [], [], data]
        else:
            news[usuario] = {news_id: [title, article, [], [], data]}
        print('\033[92mNotícia adicionada!\033[0m')
        send_email(title, usuario, perfis)

        create_more_news = input('Deseja criar mais uma notícia? [sim/nao]')
        if create_more_news == 'nao':
            break


#essa def lista todas as notícias
def adm_list_news(news, usuario):
    for x, y in news.items():
        for z in y:

            if x == usuario:
                print(f'Autor: {x}')
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
        remove_options = int(input(
            '[1]Excluir uma notícia\n'
            '[2]Excluir todas as notícias\n'
        ))
        if remove_options == 1:
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

        elif remove_options == 2:
            news.pop(usuario)
            print('\033[92mTodas as notícia foram removidas!\033[0m')
            break

        else:
            print('\033[91mOpção inválida!\033[0m')
            break


#essa def é para editar uma notícia
def adm_edit_news(news, usuario):
    while True:
        id_to_edit = int(input('Informe o id da noticia para edita-la:'))
        if id_to_edit in news[usuario]:
            edit_options = int(input(
                '[1]Editar título\n'
                '[2]Editar corpo\n'
                '[3]Editar toda a notícia\n'
            ))

            if edit_options == 1:
                new_title = input('Novo título:')
                news[usuario][id_to_edit][0] = new_title
                print('\033[92mNotícia salva!\033[0m')
                break

            elif edit_options == 2:
                new_article = input('Novo corpo:')
                news[usuario][id_to_edit][1] = new_article
                print('\033[92mNotícia salva!\033[0m')
                break

            elif edit_options == 3:
                new_title = input('Novo título:')
                news[usuario][id_to_edit][0] = new_title
                new_article = input('Novo corpo:')
                news[usuario][id_to_edit][1] = new_article
                print('\033[92mNotícia salva!\033[0m')
                break

            else:
                print('\033[91mOpção Inválida!\033[0m')

        else:
            print('\033[91mID inexistente!\033[0m')


#essa def serve para buscar noticias
def adm_search_news(news):
    while True:
        found = False
        id_to_search = int(input('Informe o ID da notícia para buscá-la:'))

        for x, y in news.items():
            if id_to_search in y:
                print(f'\033[96mAutor: {x}\033[0m')
                print(f'Título: {y[id_to_search][0]}')
                print(f'Artigo: {y[id_to_search][1]}')
                print('_' * 26)
                found = True

        if not found:
            print('\033[91mID inexistente!\033[0m')
        break


#essa def serve para rankear os noticias mais curtidas do usuario(adm)
def adm_rank_news(news, usuario, my_news_rank):
    if usuario in news:
        for i, j in news[usuario].items():
            my_news_rank[i] = len(j[3])

        list_news_rank = list(my_news_rank.items())

        z = len(list_news_rank)
        for x in range(z):
            for y in range(0, z - x - 1):
                if list_news_rank[y][1] < list_news_rank[y + 1][1]:
                    aux = list_news_rank[y]
                    list_news_rank[y] = list_news_rank[y + 1]
                    list_news_rank[y + 1] = aux

        for a in list_news_rank:
            print(f'Autor: {usuario}')
            print(f'Publicado em: {news[usuario][a[0]][4]}')
            print(f'Título: {news[usuario][a[0]][0]}')
            print(f'Artigo: {news[usuario][a[0]][1]}')
            comment = ', '.join(news[usuario][a[0]][2])
            print(f'Comentários: {comment}') if comment else ''
            print(f'{a[1]}❤️')
            print('_'*26)

    else:
        print(f'\033[91m{usuario} não publicou nenhuma notícia!\033[0m')


#essa def serve para mostrar o rank com as noticias com mais curtidas
def adm_geral_news_rank(news, geral_news_rank):
    for i, j in news.items():
        for k, m in j.items():
            geral_news_rank[i] = [k, len(m[3])]

    list_geral_rank = list(geral_news_rank.items())

    z = len(list_geral_rank)
    for x in range(z):
        for y in range(0, z - x - 1):
            if list_geral_rank[y][1][1] < list_geral_rank[y + 1][1][1]:
                aux = list_geral_rank[y]
                list_geral_rank[y] = list_geral_rank[y + 1]
                list_geral_rank[y + 1] = aux

    for a in list_geral_rank:
        author = a[0]
        id_news = a[1][0]
        print(f'Autor: {author}')
        print(f'Publicado em: {news[author][id_news][4]}')
        print(f'Título: {news[author][id_news][0]}')
        print(f'Artigo: {news[author][id_news][1]}')
        comment = ' ,'.join(news[author][id_news][2])
        print(f'Comentários: {comment}') if comment else ''
        print(f'{a[1][1]}❤️')
        print('_'*26)


#essa def serve para fazer o download de todas as noticias do adm
def adm_download_news(news, list_download_news, usuario):
    for x, y in news.items():
        for z in y:
            if x == usuario:
                author = x + '\n'
                title = y[z][0] + '\n'
                article = y[z][1] + '\n'
                list_download_news.append({'Autor': author, 'Título': title, 'Artigo': article})

    with open(f'{usuario}.txt', 'w') as f:
        for a in list_download_news:
            b = a['Autor']
            c = a['Título']
            d = a['Artigo']

            texto = f'Autor: {b}'
            texto += f'Titulo: {c}'
            texto += f'Artigo: {d}'

            f.write(texto + '\n')

    print('\033[35mAguarde o download das suas notícias!\033[0m')
