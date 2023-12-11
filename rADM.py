import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#def para enviar emails
def send_email(title, usuario, perfis):
    for i, j in perfis.items():
        if j[0] == '1':
            for k in j[3]:
                #configurações do servidor SMTP do gmail
                servidor_smtp = "smtp.gmail.com"
                porta_smtp = 587

                #informações da conta de e-mail
                sender_email = SEU EMAIL
                sender_password = SUA SENHA


                mensagem = MIMEMultipart()
                mensagem["From"] = sender_email
                mensagem["To"] = k
                mensagem["Subject"] = f'{usuario} postou uma nova notícia!'

                #adicionando corpo da mensagem
                mensagem.attach(MIMEText(title, "plain"))

                #configurando a conexao SMTP
                servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
                servidor.starttls()

                #logando na conta de e-mail
                servidor.login(sender_email, sender_password)

                #enviando o e-mail
                servidor.sendmail(sender_email, k, mensagem.as_string())

                #fechando a conexao SMTP
                servidor.quit()


#def para inserir noticias
def adm_insert_news(news, id, usuario, perfis):
    while True:
        title = input('Título:')
        article = input('Corpo da Notícia:')
        data = input('Insira a data de publicação da notícia no formato dia/mês/ano:')
        news_id = id[0] + 1
        id[0] = news_id

        #verifica se o usuario ja postou alguma noticia
        if usuario in news:
            #se ja postou alguma noticia ele cria um novo id
            news[usuario][news_id] = [title, article, [], [], data]
        else:
            #senao ele cria um nova chave
            news[usuario] = {news_id: [title, article, [], [], data]}
        print('\033[92mNotícia adicionada!\033[0m')

        #envia um email contendo o titulo da noticia para todos os usuario que o favoritaram
        send_email(title, usuario, perfis)

        create_more_news = input('Deseja criar mais uma notícia? [sim/nao]')
        if create_more_news == 'nao':
            break


#def para listar todas as noticias do adm
def adm_list_news(news, usuario):
    for x, y in news.items():
        for z in y:
            #verifica se a noticia que ira ser listada é do adm
            if x == usuario:
                #printa todas as informações da noticia
                print(f'ID: {z}')
                print(f'Autor: {x}')
                print(f'Publicado em {y[z][4]}')
                print(f'Título: {y[z][0]}')
                print(f'Artigo: {y[z][1]}')
                comment = ', '. join(y[z][2])
                print(f'Comentários: {comment}') if comment else ''
                print(f'{len(y[z][3])}❤️')
                print('_'*26)


#def para remover as noticias do adm
def adm_remove_news(news, usuario):
    while True:
        remove_options = int(input(
            '[1]Excluir uma notícia\n'
            '[2]Excluir todas as notícias\n'
        ))
        if remove_options == 1:
            id_to_remove = int(input('Informe o id da noticia para remove-la:'))

            #verifica se o id informado existe no dicionario
            if id_to_remove in news[usuario]:
                #remove a noticia
                news[usuario].pop(id_to_remove)
                print('\033[92mNotícia removida!\033[0m')
                y = input('Deseja remover mais notícias? [sim/nao]')
                if y == 'nao':
                    break
            else:
                print('\033[91mID inexistente!\033[0m')
                break

        elif remove_options == 2:
            #remove todas as noticias postadas pelo o adm
            news.pop(usuario)
            print('\033[92mTodas as notícia foram removidas!\033[0m')
            break

        else:
            print('\033[91mOpção inválida!\033[0m')
            break


#def para editar a noticia do adm
def adm_edit_news(news, usuario):
    while True:
        id_to_edit = int(input('Informe o id da noticia para edita-la:'))
        #verifica se o id informado existe no dicionario
        if id_to_edit in news[usuario]:
            edit_options = int(input(
                '[1]Editar título\n'
                '[2]Editar corpo\n'
                '[3]Editar toda a notícia\n'
            ))

            if edit_options == 1:
                new_title = input('Novo título:')
                #edita apenas o titulo
                news[usuario][id_to_edit][0] = new_title
                print('\033[92mNotícia salva!\033[0m')
                break

            elif edit_options == 2:
                new_article = input('Novo corpo:')
                #edita o corpo da noticia
                news[usuario][id_to_edit][1] = new_article
                print('\033[92mNotícia salva!\033[0m')
                break

            elif edit_options == 3:
                #edita toda a noticia
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


#def para buscar noticias
def adm_search_news(news):
    found = False
    search = input('Pesquisa:')
    #procura search no indice 0 (contem o titulo) da lista, se tiver printa toda a noticia
    for autor, dicionario in news.items():
        for id_news, lista in dicionario.items():
            if search in lista[0]:
                found = True
                print(f'ID: {id_news}')
                print(f'Autor: {autor}')
                print(f'Publicado em {lista[4]}')
                print(f'Título: {lista[0]}')
                print(f'Artigo: {lista[1]}')
                comment = ', '.join(lista[2])
                print(f'Comentários: {comment}') if comment else ''
                print(f'{len(lista[3])}❤️')
                print('_' * 26)

    if not found:
        print('Nenhuma notícia encontrada!')


#def para rankear as noticias mais curtidas do adm
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


#def para rankear todas as noticias
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


#def para fazer download das noticias do adm
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
