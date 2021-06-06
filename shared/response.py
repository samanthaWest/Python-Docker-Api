import datetime

def error_response(message):
    return {
        'status': 'Error',
        'message':f'{message}',
        'timestamp': datetime.now()
    }

def success_response():
    return {
            'status': 'Success',
            'timestamp': datetime.now()
        }

def exception_response():
    return {
            'status': 'Error',
            'message': 'An internal server error occured'
            'timestamp': datetime.now()
        }
