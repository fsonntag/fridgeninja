__author__ = 'dowling'
from flask import Blueprint

hello_blueprint = Blueprint("hello", __name__, url_prefix="/hello")

@hello_blueprint.route("/")
def hello_world():
    return "This works!"