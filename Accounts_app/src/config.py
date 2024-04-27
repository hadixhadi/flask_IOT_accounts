import os.path


class BaseConfig:
    BASE_DIR=os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = '8f443b236e94c467a95cd3641ca48f1dd8130a5ce9317abfb965a38d84285738'
    SECRET_KEY = 'a4de428af7226edc5de4dbdee6f414758a4f03036aa920a0d3bd29f665b9e09f'
    DB_SETTINGS = {
        "host": "mysql",
        "user": "root",
        "password": "1q2w3e4r5t",
        "database": "accountsDB"
    }



class DevConfig(BaseConfig):
    DEBUG=True

class ProductConfig(BaseConfig):
    pass