from bs4 import BeautifulSoup
from decimal import Decimal
from datetime import datetime
from models import Figure, Price
from db import db
BASE_URL = 'http://www.raccoongames.es'

async def process_page(html):
    soup = BeautifulSoup(html)
    products = soup.find_all('div', 'producto-lst')

    for product in products:
        await process_product(product)


async def process_product(product):
    print("Procesando producto: {}".format(product.img['alt']))
    data = {
        'name' : product.img['alt'],
        'image' : '{}{}'.format(BASE_URL, product.img['src']),
        'price' : float(Decimal(product.find_all('span', 'precio-actual')[0].text[2:].replace(',','.')))
    }
    
    try:
        figure = Figure.objects.get(name=data['name'])
    except Figure.DoesNotExist:
        figure = Figure.objects.create(
            name = data['name'],
            image = data['image']
        )

    price = Price(
        date = datetime.now(),
        amount = data['price']
    )
    figure.prices.append(price)
    figure.save()