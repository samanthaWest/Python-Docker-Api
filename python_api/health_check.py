from sanic.response import json

@s.route('/health')
async def health_check(request):
    """ Status Endpoint """
    return json(
        {
            "status": "alive"
        }
    )