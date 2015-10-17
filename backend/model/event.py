__author__ = 'dowling'
from model.db import connection
from mongokit import Document
from model.user import User
import datetime

class Event(Document):
    structure = {
        'user': User,
        'timestamp': datetime.datetime,
        'transactions': {
            unicode: int
        },
    }
    use_dot_notation = True
    use_autorefs = True

connection.register([Event])
