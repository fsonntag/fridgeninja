__author__ = 'dowling'
from model.db import connection
from mongokit import Document
from model.db import connection
from model.user import User

class Fridge(Document):
    structure = {
        'users': [User],
        'content': {
            unicode: int
        },
        'users': [User]
    }

    user_autorefs = True
    use_dot_notation = True

connection.register([Fridge])
