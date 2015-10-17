__author__ = 'dowling'

from mongokit import Document
from model.db import connection

class User(Document):
    use_autorefs = True
    use_dot_notation = True
    structure = {
        'name': unicode,
        'events': list,
        'device': unicode
    }

    use_autorefs = True
    use_dot_notation = True

connection.register([User])
