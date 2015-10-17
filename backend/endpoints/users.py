__author__ = 'dowling'
import logging
ln = logging.getLogger(__name__)
from flask import request, Blueprint, jsonify
from model.db import db
from bson.objectid import ObjectId


user_blueprint = Blueprint("user", __name__, url_prefix="/users")

user_collection = db.users


@user_blueprint.route("/", methods=["POST"])
def post_user():
    data = request.get_json(force=True)

    user = user_collection.User()
    user.name = data['name']
    user.events = []
    user.device = data['device']
    user.save()
    # ln.debug(type(user.to_json()))

    return jsonify(user=user.to_json_type())



@user_blueprint.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    user = user_collection.User.get_from_id(ObjectId(user_id))
    return jsonify(user.to_json_type())


@user_blueprint.route("/", methods=["GET"])
def get_users():
    users = user_collection.User.find()
    return jsonify(users=[user.to_json_type() for user in users])
