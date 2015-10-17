__author__ = 'dowling'
from model.db import connection
from mongokit import Document
from model.user import User
import datetime

class Event(Document):
    structure = {
        'user': unicode,
        'timestamp': datetime.datetime,
        'transactions': [{
            'item': unicode,
            'quantity': int
        }]
    }
    use_dot_notation = True

connection.register([Event])
