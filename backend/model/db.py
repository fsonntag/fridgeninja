__author__ = 'dowling'
from mongokit import Connection

# configuration
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

connection = Connection(MONGODB_HOST, MONGODB_PORT)
db = connection.testdb