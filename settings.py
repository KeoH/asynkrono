import os
from db import db
import aiohttp_jinja2, jinja2
from views import setup_views
from aiohttp import web

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
TEMPLATES_ROOT = os.path.join(BASE_DIR, 'templates')

PAGINATION = 10

MIDDLEWARES = [

]

app = web.Application(
    middlewares = MIDDLEWARES
)

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
