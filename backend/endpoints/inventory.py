__author__ = 'dowling'

from flask import Blueprint, jsonify
from model.db import db

fridge_blueprint = Blueprint("inventory", __name__, url_prefix="/inventory")

fridge_collection = db.fridge


@fridge_blueprint.route("/", methods=["GET"])
def get_inventory():
    fridge = fridge_collection.Fridge.find_one()
    return jsonify(inventory=fridge.content.to_json_type())