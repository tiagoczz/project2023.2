import smtplib
import email.message


#essa def envia o e-mail para o admin, informando que sua notícia teve um comentário e exibe qual foi o comentário
# vou ajeitar dps
'''def send_email(email_adm, comment, id):
    x = email_adm[id][0]
    y = comment[id][1]

    msg = email.message.Message()
    msg['Subject'] = 'Comentaram na sua notícia'
    msg['From'] = 'jamesbot.ifpb@gmail.com'
    msg['To'] = x
    password = 'lied uthj dsde rdax'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(y)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('E-mail enviado')'''


#essa def serve para o usuário buscar uma noticia
def user_search_news(all_news, body_news, data_news, send_email):
    emoji_like = '👍'
    while True:
        search_id = int(input('Informe o ID da notícia para busca-la:'))
        if search_id in all_news:
            print(all_news[search_id][0])
            print(body_news[search_id])
            comment_question = input('Deseja fazer um comentário? sim/nao')
            if comment_question == 'sim':
                while True:
                    comment = input('Comentário:')
                    all_news[search_id].append(comment)
                    print('Comentário adicionado')
                    send_email(data_news, all_news, search_id)
                    yes_or_no = input('Ainda quer comentar mais alguma coisa? sim/nao')
                    if yes_or_no == 'nao':
                        break
                like_question = input('Deseja curtir essa notícia? sim/nao')
                if like_question == 'sim':
                    all_news[search_id].append(emoji_like)

            yes_or_no = input('Deseja continuar procurando? sim/nao')
            if yes_or_no == 'nao':
                break

        else:
            print('Não existe nenhuma notícia com esse ID.')
            yes_or_no = input('Deseja continuar procurando? sim/nao')
            if yes_or_no == 'nao':
                break


#essa def serve para o usuário comentar na notícia
def user_comment_news(all_news, data_news, send_email):
    comment_id = int(input('Informe o ID da notícia para comentar:'))
    if comment_id in all_news:
        while True:
            comment = input('Comentário:')
            all_news[comment_id].append(comment)
            print('Comentário adicionado')
            send_email(data_news, all_news, comment_id)
            yes_or_no = input('Ainda quer comentar mais alguma coisa? sim/nao')
            if yes_or_no == 'nao':
                break


#essa def serve para o usuário curtir a notícia
def user_like_news(all_news):
    emoji_like = '👍'
    like_id = int(input('Informe o ID da notícia para curti-la:'))
    if like_id in all_news:
        all_news[like_id].append(emoji_like)


#essa def serve para o usuário listar as notícias
def user_list_news(all_news, body_news):
    print('Essas são todas as notícias.')
    for key, valor in all_news.items():
        print(f'ID({key}): {valor[0]}')
        print(f'{body_news[key]}')
        print(f'Comentários: {valor[1]}')
