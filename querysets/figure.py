from mongoengine import QuerySet

from settings import PAGINATION

class FigureQueryset(QuerySet):

    def page(self, page = 1):
        init_value = PAGINATION * (page-1)
        last_value = (PAGINATION * page)
        return self[init_value:last_value]