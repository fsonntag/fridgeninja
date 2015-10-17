__author__ = 'dowling'
import logging
ln = logging.getLogger(__name__)

from flask import request, Blueprint, jsonify
from model.db import db

user_blueprint = Blueprint("user", __name__, url_prefix="/user")

user_collection = db.user


@user_blueprint.route("", methods=["POST"])
def post_user():
    data = request.get_json(force=True)

    # user_collection.find_one({'name': data['name']})


    user = user_collection.User()
    user.name = data['name']
    user.events = []
    user.device = data['device']
    user.save()

    ln.debug("Posted user %s with device %s and ID %s" % (user.name, user.device, user._id))
    return "Posted user %s with device %s and ID %s" % (user.name, user.device, user._id)

@user_blueprint.route("", methods=["GET"])
def get_user():
    pass
