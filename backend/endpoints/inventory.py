__author__ = 'dowling'

from flask import Blueprint, jsonify
from model.fridge import fridge
from bson.objectid import ObjectId

fridge_blueprint = Blueprint("inventory", __name__, url_prefix="/inventory")




@fridge_blueprint.route("/", methods=["GET"])
def get_inventory():
    return jsonify(inventory=fridge.to_json_type())