__author__ = 'dowling'
import logging
ln = logging.getLogger(__name__)
from flask import request, Blueprint, jsonify, abort
from model.db import db
from bson.objectid import ObjectId


user_blueprint = Blueprint("user", __name__, url_prefix="/users")

user_collection = db.user


@user_blueprint.route("/", methods=["POST"])
def post_user():
    data = request.get_json(force=True)

    user = user_collection.User.find_one({"name": data["username"]})
    if user:
        ln.warn("Tried to post user with name %s, but already exists. Aborted.".format(data["name"]))
        abort(409)
        return "User already exists"

    user = user_collection.User()
    user.name = data['username']
    user.events = []
    user.device = data['device']
    user.save()

    return jsonify(user=user.to_json_type())


@user_blueprint.route("/<username>", methods=["GET"])
def get_user(username):
    user = user_collection.User.find_one({"name": username})
    return jsonify(user.to_json_type())




@user_blueprint.route("/", methods=["GET"])
def get_users():
    users = user_collection.User.find()
    return jsonify(users=[user.to_json_type() for user in users])
