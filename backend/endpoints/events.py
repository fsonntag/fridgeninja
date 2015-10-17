__author__ = 'dowling'
from flask import request, Blueprint, jsonify


events_blueprint = Blueprint("events", __name__, url_prefix="/events")

@events_blueprint.route("/", methods=["POST"])
def post_event():
    data = request.get_json(force=True)
    # TODO read data from json (what was taken/added, who did it, etc)

    return


@events_blueprint.route("/", methods=["GET"])
def get_events():
    # TODO read data all events and return them

    return

@events_blueprint.route("/<event_id>", methods=["GET"])
def get_event(event_id):
    # TODO read data for this event

    return