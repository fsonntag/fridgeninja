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
    #validators = {
    #    'name': max_length(50),
    #    'email': max_length(120)
    #}

    # timestamp
    # user
    # transaction items and counts
    pass

conn.register([Event])