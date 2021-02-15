import imaplib
import email
from email.header import decode_header

from email_task.config import EmailConfig


# учетные данные
username = EmailConfig.username
password = EmailConfig.password

# create an IMAP4 class with SSL
imap = imaplib.IMAP4_SSL("imap.yandex.ru")
# authenticate
imap.login(username, password)

# select the mailbox I want to delete in
# if you want SPAM, use imap.select("SPAM") instead
imap.select("INBOX")

# поиск определенных писем по отправителю
status, messages = imap.search(None, "FROM", "robot@konturcheck.ru")

# преобразовать сообщения в список адресов электронной почты
messages = messages[0].split(b' ')

for mail in messages:
    _, msg = imap.fetch(mail, "(RFC822)")
    # вы можете удалить цикл for для повышения производительности, если у вас длинный список писем
    # потому что он предназначен только для печати SUBJECT целевого электронного письма, которое нужно удалить
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            # расшифровать тему письма
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                # if it's a bytes type, decode to str
                subject = subject.decode()
            print("Deleting", subject)
    # отметить письмо как удаленное
    imap.store(mail, "+FLAGS", "\\Deleted")

# навсегда удалить письма, помеченные как удаленные
# из выбранного почтового ящика (в данном случае INBOX)
imap.expunge()
# закрыть почтовый ящик
imap.close()
# выйти из аккаунта
imap.logout()
