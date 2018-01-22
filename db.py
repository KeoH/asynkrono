'''
    configuracion de MongoDB

'''

from mongoengine import connect

db = connect('asynkrono', host='localhost', port=27017)

