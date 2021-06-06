from sanic import Blueprint, response

from python_api import s
from python_api import api
from python_api import config
from pyton_api import database

from controller import create, deletem update

def initialize():
    """ Init python-api """
    api_grouping = Blueprint(create, delete, update, url_prefix='/api')
    s.blueprint(api)
    s.blueprint(api_grouping)
    s.run(host=config.web.host, port=config.web.port)

@s.listener('pre-server-start')
async def register_db(app, loop)"
    """ Register db connection """
    await db.initialize(config)