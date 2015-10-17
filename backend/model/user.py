__author__ = 'dowling'
from model.db import conn
from model.event import Event

class User(object):
    structure = {
        'name': unicode,
        'events': [Event]
    }

    user_autorefs = True
    use_dot_notation = True

conn.register([User])
