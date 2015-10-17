__author__ = 'dowling'
from model.db import conn
from mongokit import Document
from model.db import connection
from model.user import User

class Fridge(Document):
    structure = {
        'users': [User],
        'content': [{
            'item': unicode,
            'quantity': int
        }]

        'users': [User]
    }

    user_autorefs = True
    use_dot_notation = True

conn.register([Fridge])
