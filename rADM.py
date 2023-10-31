#essa def serve para inserir noticias
def adm_insert_news(all_news, body_news, data_news):
    while True:
        news_id = int(input('Crie um ID para a sua notícia:'))
        email_adm = input('Informe seu e-mail:')
        for i in all_news.keys():
            if i == news_id:
                print('Você não pode informar o mesmo ID.')
                news_id = int(input('Crie um outro ID:'))

        title_news = input('Insira o título da sua notícia:')
        all_news[news_id] = [title_news]
        news = input('Insira o corpo da sua notícia:')
        body_news[news_id] = [news]
        data_news[news_id].append(email_adm)
        yes_or_no = input('Ainda quer inserir notícias? sim/nao')
        if yes_or_no == 'nao':
            break


#essa def lista todas as notícias
def adm_list_news(all_news, body_news):
    print('Essas são todas as notícias.')
    for key, valor in all_news.items():
        print(f'ID({key}): {valor[0]}')
        print(f'{body_news[key]}')


#essa def remove uma notícia
def adm_remove_news(all_news, body_news):
    while True:
        remove_id = int(input('Informe o ID da notícia para remove-la:'))
        if remove_id in all_news and remove_id in body_news:
            all_news.pop(remove_id)
            body_news.pop(remove_id)
            yes_or_no = input('Ainda quer remover uma noticia? sim/nao')
            if yes_or_no == 'nao':
                break

        else:
            print('ID inexistente!')
            yes_or_no = input('Ainda quer remover uma noticia? sim/nao')
            if yes_or_no == 'nao':
                break


#essa def é para winicius fazer e consertar
'''def winicius():
    while True:
        edit_id = int(input('Informe o ID da notícia que deseja editar:'))
        if edit_id in all_news:
            all_news.pop(edit_id)
            question = input('Edite a notícia:')
            all_news[edit_id] = [question]
            yes_or_no = input('Deseja editar mais alguma coisa? sim/nao')
            if yes_or_no == 'nao':
                break
            else:
                print('Não existe nenhuma notícia relacionada a esse ID.')
                yes_or_no = input('Deseja editar mais alguma coisa? sim/nao')
                if yes_or_no == 'nao':
                    break'''


#essa def serve para buscar notícias
def adm_search_news(all_news, body_news):
    while True:
        search_id = int(input('Informe o ID da notícia para busca-la:'))
        if search_id in all_news and search_id in body_news:
            print(all_news[search_id][0])
            print(body_news[search_id])
            yes_or_no = input('Deseja continuar procurando? sim/nao')
            if yes_or_no == 'nao':
                break
        else:
            print('Digite algo válido')
            yes_or_no = input('Deseja continuar procurando? sim/nao')
            if yes_or_no == 'nao':
                break
