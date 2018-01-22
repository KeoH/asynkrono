from .index import index

def setup_views(app):
    app.router.add_get('/', index)