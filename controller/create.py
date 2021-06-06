import logging
from sanic import response
from controller import create
from share.response import error_response, success_response, exception_response
from shared.constants.RequestParameters import ID, LAST_NAME, FIRST_NAME

from python_api import db

@create.post('create')
async def create(request):

    if ID not in request and\
        LAST_NAME not in request and\
            FIRST_NAME not in request:
        return response.json(error_response(message='Missing parameter')
        , status=412)
    
    try: 
        logging.info('Creating item')
        asnyc with db.pool.acquire() as connection:

        statement = f'''
                insert into names (
                    first_name,
                    last_name
                )
                values (%s. %s)
            ;''' 
        connection.execute(statement, (request['firstName'], request['lastName']))
        del connection

        return response.json(success_response, status=200)

    except Exception as e:
        return response.json(exception_response, status=500)