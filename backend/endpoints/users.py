__author__ = 'dowling'
import logging
ln = logging.getLogger(__name__)
from flask import request, Blueprint, jsonify
from model.db import db
from bson.objectid import ObjectId

user_blueprint = Blueprint("user", __name__, url_prefix="/user")

user_collection = db.user


@user_blueprint.route("/", methods=["POST"])
def post_user():
    data = request.get_json(force=True)

    # user_collection.find_one({'name': data['name']})
    #TODO check if exists


    user = user_collection.User()
    user.name = data['name']
    user.events = []
    user.device = data['device']
    user.save()
    # ln.debug(type(user.to_json()))
    return jsonify(user = user.to_json_type())


@user_blueprint.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    user = user_collection.User.get_from_id(ObjectId(user_id))
    return jsonify(user.to_json_type())

#TODO get all users