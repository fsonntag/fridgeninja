__author__ = 'dowling'
import logging
ln = logging.getLogger(__name__)
from flask import request, Blueprint, jsonify, abort
from model.db import db


user_blueprint = Blueprint("user", __name__, url_prefix="/users")

user_collection = db.users


@user_blueprint.route("/", methods=["POST"])
def post_user():
    data = request.get_json(force=True)

    user = user_collection.User.find_one({"username": data["username"]})
    if user:
        ln.warn("Tried to post user with name %s, but already exists. Aborted.".format(data["username"]))
        abort(409)
        return "User already exists"

    user = user_collection.User()
    user.username = data['username']
    user.events = []
    user.device = data['device']
    user.save()

    return jsonify(user=user.to_json_type())


@user_blueprint.route("/<username>", methods=["GET"])
def get_user(username):
    user = user_collection.User.find_one({"username": username})
    return jsonify(user.to_json_type())




@user_blueprint.route("/", methods=["GET"])
def get_users():
    users = user_collection.User.find()
    return jsonify(users=[user.to_json_type() for user in users])
