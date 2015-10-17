__author__ = 'dowling'
from model.db import conn
from mongokit import Document
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

conn.register([Event])