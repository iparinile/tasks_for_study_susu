from dotenv import load_dotenv
from os import getenv

load_dotenv()


class EmailConfig:
    username = getenv('email_username', 'username')
    password = getenv('email_password', 'qwerty')
