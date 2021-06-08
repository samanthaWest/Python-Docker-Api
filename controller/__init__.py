from sanic import Blueprint

 create = Blueprint('create', url_prefix='/v2')
 delete = Blueprint('delete', url_prefix='/v2')
 update = Blueprint('update', url_prefix='/v2')
