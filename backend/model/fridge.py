__author__ = 'dowling'
import logging
ln = logging.getLogger(__name__)
from mongokit import Document
from model.db import connection
from model.db import db


class Fridge(Document):
    structure = {
        'content': {
            unicode: int
        }
    }
    use_dot_notation = True
    use_autorefs = True

    def transact_item(self, item, quantity):

        old_quantity = self.content.get(item, None)
        print item, quantity, old_quantity

        if quantity < 0:  # take out
            if old_quantity is None:
                old_quantity = 0
                ln.warn("Attempting to take item %s out of fridge, but previous value was %s" % (item, old_quantity))

        else:  # put in
            if old_quantity is None:
                old_quantity = 0


                ln.warn("Adding new item %s (quantity %s)" % (item, old_quantity))
            ln.debug("Putting %s of %s into fridge" % (quantity, item))
        print old_quantity
        self.content[item] = old_quantity + quantity

connection.register([Fridge])

fridge_collection = db.fridges
#fridge = fridge_collection.Fridge()
#fridge.save()
#fridge.reload()

def get_fridge():
    fs = list(fridge_collection.Fridge.find())
    for f in fs:
        if f.content:
            return f
    if not fs:
        f = fridge_collection.Fridge()
        f.save()
        f.reload()
        return f
    else:
        return fs[0]

