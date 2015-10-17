__author__ = 'dowling'
from fridge_server import app
from mongokit import Connection

# configuration
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

conn = Connection(MONGODB_HOST, MONGODB_PORT)