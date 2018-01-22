from datetime import datetime

from mongoengine import Document, StringField, DateTimeField
from mongoengine import DecimalField, URLField, ListField, queryset_manager
from mongoengine import EmbeddedDocumentListField, EmbeddedDocument

from querysets import FigureQueryset


class Price(EmbeddedDocument):
    amount = DecimalField()
    date = DateTimeField()


class Figure(Document):
    name = StringField(max_length=255, required=True)
    image = URLField()
    prices = EmbeddedDocumentListField(Price, default=[])

    meta = {
        'queryset_class' : FigureQueryset
    }

    @property
    def price(self):
        return self.prices[-1]