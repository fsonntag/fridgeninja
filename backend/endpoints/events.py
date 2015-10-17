__author__ = 'dowling'
import logging
ln = logging.getLogger(__name__)

from flask import request, Blueprint, jsonify
from model.db import db
import datetime
from model.fridge import fridge

events_blueprint = Blueprint("events", __name__, url_prefix="/events")

fridge_collection = db.fridges
event_collection = db.events
user_collection = db.users

@events_blueprint.route("/", methods=["POST"])
def post_event():
    data = request.get_json(force=True)

    user = user_collection.User.find_one({"username": data["username"]})

    if user is None:
        raise ValueError("No user with that name was found!")

    event = event_collection.Event()

    event.timestamp = datetime.datetime.now()
    transactions = data["transactions"]
    event.transactions = transactions
    event.user = user
    event.save()

    for item, quantity in transactions.items():
        fridge.transact_item(item, quantity)

    fridge.save()

    return jsonify(event=event.to_json_type())


@events_blueprint.route("/", methods=["GET"])
def get_events():
    # TODO: limit to x most recent
    events = event_collection.Event.find()
    return jsonify(events=[event.to_json_type() for event in events])


@events_blueprint.route("/<event_id>", methods=["GET"])
def get_event(event_id):
    event = event_collection.Event.get_from_id(event_id)
    return jsonify(event=event.to_json())
