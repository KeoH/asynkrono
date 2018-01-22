from mongoengine import QuerySet

import settings

class FigureQueryset(QuerySet):

    def page(self, page = 1):
        init_value = settings.PAGINATION * (page-1)
        last_value = (settings.PAGINATION * page)
        return self[init_value:last_value]