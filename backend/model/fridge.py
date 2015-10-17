__author__ = 'dowling'
from model.db import conn
from mongokit import Document
from model.user import User

class Fridge(Document):
    structure = {
        'users': [User],
        'content': [{
            'item': unicode,
            'quantity': int
        }]


    }

    user_autorefs = True
    use_dot_notation = True

conn.register([Fridge])