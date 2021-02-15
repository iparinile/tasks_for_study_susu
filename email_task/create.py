import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup as bs

from email_task.config import EmailConfig


def create_mail(subject: str, mail_body: str, recipient: str):
    # ваши учетные данные
    email = EmailConfig.username
    password = EmailConfig.password
    # электронная почта отправителя
    FROM = EmailConfig.username
    # адрес электронной почты получателя
    TO = recipient
    # тема письма (тема)
    subject = subject

    # инициализируем сообщение, которое хотим отправить
    msg = MIMEMultipart("alternative")
    # установить адрес электронной почты отправителя
    msg["From"] = FROM
    # установить адрес электронной почты получателя
    msg["To"] = TO
    # задаем тему
    msg["Subject"] = subject

    # установить тело письма как HTML
    html = mail_body
    # делаем текстовую версию HTML
    text = bs(html, "html.parser").text

    text_part = MIMEText(text, "plain")
    html_part = MIMEText(html, "html")
    # прикрепить тело письма к почтовому сообщению
    # сначала прикрепите текстовую версию
    msg.attach(text_part)
    msg.attach(html_part)

    return email, password, FROM, TO, msg


def send_mail(email, password, FROM, TO, msg):
    # инициализировать SMTP-сервер
    server = smtplib.SMTP("smtp.yandex.ru", 587)
    # подключиться к SMTP-серверу в режиме TLS (безопасный) и отправить EHLO
    server.starttls()
    # войти в учетную запись, используя учетные данные
    server.login(email, password)
    # отправить электронное письмо
    server.sendmail(FROM, TO, msg.as_string())
    # завершить сеанс SMTP
    server.quit()


if __name__ == '__main__':
    email, password, FROM, TO, msg = create_mail(
        subject="Just a subject",
        mail_body="""This email is sent using <b>Python</b>!""",
        recipient=EmailConfig.username
    )
    send_mail(email, password, FROM, TO, msg)
