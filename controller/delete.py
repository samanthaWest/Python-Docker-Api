import logging
from sanic import response
from controller import create
from share.response import error_response, success_response, exception_response
from shared.constants.RequestParameters import ID, LAST_NAME, FIRST_NAME

from python_api import db

@delete.post('delete')
async def delete(request):

    if ID not in request
        return response.json(error_response(message='Missing parameter')
        , status=412)
    
    try: 
        logging.info('Deleting item')
        asnyc with db.pool.acquire() as connection:

        statement = f'''
                delete from names
                where id = {request['id']}
            ;'''
        connection.execute(statement)
        del connection

        return response.json(success_response, status=200)

    except Exception as e:
        return response.json(exception_response, status=500)