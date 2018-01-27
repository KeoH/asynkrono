'''
    configuracion de MongoDB

'''

from mongoengine import connect

# Esta es la puta manera de que docker lo coja!
db = connect(host="mongodb://database/asynckrono")

