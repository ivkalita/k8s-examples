import socket

from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route('/')
async def info(request):
    return json({
        'request': {
            'headers': {k: v for k, v in request.headers.items()},
            'ip': request.socket[0],
            'port': request.socket[1],
            'url': request.url
        },
        'host': socket.gethostname()
    })


@app.route('/health')
async def health(request):
    return json({'status': 'ok'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
