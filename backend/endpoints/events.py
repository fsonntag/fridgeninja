__author__ = 'dowling'
import logging
ln = logging.getLogger(__name__)

from flask import request, Blueprint, jsonify
from model.db import db
from model.event import Event
import datetime
from bson.objectid import ObjectId
from model.fridge import fridge
events_blueprint = Blueprint("events", __name__, url_prefix="/events")

fridge_collection = db.fridges
event_collection = db.events
user_collection = db.users

@events_blueprint.route("/", methods=["POST"])
def post_event():
    data = request.get_json(force=True)

    user_id = ObjectId(data["user"])
    user = user_collection.User.get_from_id(user_id)

    if user is None:
        raise ValueError("No user with that ID was found!")

    event = event_collection.Event()

    event.timestamp = datetime.datetime.now()
    transactions = data["transactions"]
    event.transactions = transactions
    event.save()

    user.events.append(event)
    user.save()

    for item, quantity in transactions.items():
        fridge.transact_item(item, quantity)

    fridge.save()

    return jsonify(event=event.to_json_type())


@events_blueprint.route("/", methods=["GET"])
def get_events():
    events = event_collection.Event.find()
    return jsonify(events=[event.to_json_type() for event in events])

@events_blueprint.route("/<event_id>", methods=["GET"])
def get_event(event_id):
    event = event_collection.Event.get_from_id(event_id)

    return jsonify(event=event.to_json())
