'''
    Pruebas con aiohttp y mongo
'''

from aiohttp import web
from settings import app

# starts the server
web.run_app(app, host='0.0.0.0', port=8080)
