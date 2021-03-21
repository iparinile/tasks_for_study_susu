from email_task_2.create import create_mail, send_mail

to_list = []  # Список адресов для рассылки

if __name__ == '__main__':
    for recipient in to_list:
        email, password, FROM, TO, msg = create_mail(
            subject='Тестовое письмо',
            mail_body="""Тестовое письмо - <b>Ура!</b>""",
            recipient=recipient
        )
        send_mail(email, password, FROM, TO, msg)
