import aiohttp_jinja2

import settings

from models import Figure

@aiohttp_jinja2.template('index.html')
async def index(request):
    page = int(request.GET.get('page', 1))
    figures = Figure.objects.page(page)
    total_figures = Figure.objects.count()
    total_pages = int(total_figures/settings.PAGINATION)
    context = {
        'figures' : figures,
        'total_figures' : total_figures,
        'page' : page,
        'total_pages' : total_pages
    }
    return context

