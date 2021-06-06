import os

class WebConfig():
    """ Web Configiration """
    def __init__(self):
        self.host = os.environ['WEB_HOST']
        self.port = os.environ['WEB_PORT']

class DbConfig():
    """ DB Configiration """
    def __init__(self):
        self.host = os.environ['DATABASE_HOST']
        self.port = os.environ['DATABASE_PORT']
        self.name = os.environ['DATABASE_NAME']
        self.user = os.environ['DATABASE_USER']
        self.password = os.environ['DATABASE_PASS']
        self.schema = os.environ['DATABASE_SCHEMA']

class AppConfig():
    """ App Configuration """
    def __init__(self):
        self.web = WebConfig()
        self.db = DbConfig()