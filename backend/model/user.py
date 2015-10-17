__author__ = 'dowling'

from mongokit import Document
from model.db import connection

class User(Document):
    structure = {
        'name': unicode,
        'events': list
    }

    use_autorefs = True
    use_dot_notation = True

connection.register([User])
