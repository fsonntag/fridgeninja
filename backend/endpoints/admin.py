__author__ = 'dowling'

from flask import Blueprint, jsonify
from model.db import connection

admin_blueprint = Blueprint("admin", __name__, url_prefix="/admin")

@admin_blueprint.route("/reset_db", methods=["GET"])
def get_inventory():
    connection.drop_database("testdb")
    return jsonify(status=200)