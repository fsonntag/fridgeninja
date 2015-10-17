__author__ = 'dowling'
from mongokit import Document
from model.db import connection
from model.user import User


class Fridge(object):
    structure = {
        'content': [{
            "item": unicode,
            "quantity": int
        }],
        'users': [User]
    }
    use_dot_notation = True

connection.register([Fridge])