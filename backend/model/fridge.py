__author__ = 'dowling'
import logging
ln = logging.getLogger(__name__)
from mongokit import Document
from model.db import connection
from model.user import User



class Fridge(object):
    structure = {
        'content': {
            unicode: int
        },
        'users': [User]
    }
    use_dot_notation = True

    def take_item(self, item, quantity):
        old_quantity = self.content.get(item, None)
        if item is None:
            ln.warn("Attempting to take item %s out of fridge, but previous value was %s" % (item, old_quantity))
            old_quantity = 0

        self.content[item] = old_quantity - quantity

    def put_item(self, item, quantity):
        ln.debug("Putting %s of %s into fridge" % (quantity, item))
        old_quantity = self.content.get(item, 0)
        self.content[item] = old_quantity + quantity



connection.register([Fridge])