__author__ = 'dowling'
from model.db import connection
from mongokit import Document
from model.user import User
import datetime


class Event(Document):
    use_dot_notation = True
    use_autorefs = True
    structure = {
        'timestamp': datetime.datetime,
        'transactions': {
            unicode: int
        },
    }


connection.register([Event])
