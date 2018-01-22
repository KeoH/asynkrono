import os
from db import db
import aiohttp_jinja2, jinja2
from views import setup_views
from aiohttp import web

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
TEMPLATES_ROOT = os.path.join(BASE_DIR, 'templates')

PAGINATION = 20
