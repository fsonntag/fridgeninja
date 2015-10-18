__author__ = 'dowling'

from flask import Blueprint, jsonify
from model.fridge import get_fridge

fridge_blueprint = Blueprint("inventory", __name__, url_prefix="/inventory")


@fridge_blueprint.route("/", methods=["GET"])
def get_inventory():
    fridge = get_fridge()
    return jsonify(inventory=[{"name": item, "quantity": count} for item, count in fridge.content.items()])


@fridge_blueprint.route("/choices", methods=["GET"])
def get_item_suggestions():
    fridge = get_fridge()
    return jsonify(suggestions=[item for item, count in sorted(fridge.content.items(), key=lambda (i,c): -int(c))])