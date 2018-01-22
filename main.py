'''
    Pruebas con aiohttp y mongo
'''

from aiohttp import web
import aiohttp_jinja2, jinja2
from db import db
from views import setup_views
import asyncio, websockets
from settings import BASE_DIR, STATIC_ROOT, TEMPLATES_ROOT


app = web.Application()

# template engine config
aiohttp_jinja2.setup(
    app, loader = jinja2.FileSystemLoader(TEMPLATES_ROOT)
)

# view routing
setup_views(app)

#static files config
app.router.add_static('/static/',
    path = STATIC_ROOT,
    name = 'static')


# starts the server
web.run_app(app, host='127.0.0.1', port=8080)