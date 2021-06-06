import os
from sanic import Sanic, Blueprint

from python_api.config import AppConfig
from python_api.config import DbConfig

CONFIG_DIR = 'configs'
config = AppConfig()

s = Sanic()
api = Blueprint('api', url_prefix='/api/v1')
db = DBConnector()