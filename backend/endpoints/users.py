__author__ = 'dowling'

from flask import Blueprint, jsonify
from model.db import db

user_blueprint = Blueprint("user", __name__, url_prefix="/user")

user_collection = db.user


@user_blueprint.route("/", methods=["POST"])
def post_user():
    user = user_collection.user.find_one()
    return jsonify(inventory=user.content.to_json())