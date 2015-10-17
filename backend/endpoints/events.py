__author__ = 'dowling'
from flask import request, Blueprint, jsonify
from model.db import db
from model.event import Event
import datetime
events_blueprint = Blueprint("events", __name__, url_prefix="/events")

fridge_collection = db.fridges
event_collection = db.events
user_collection = db.users

@events_blueprint.route("/", methods=["POST"])
def post_event():
    data = request.get_json(force=True)

    user_id = data["user"]
    user = user_collection.User.find_one({"_id": user_id})

    event = event_collection.Event()

    event.user = user
    event.timestamp = datetime.datetime.now()
    transactions = data["transactions"]
    event.transactions = transactions
    event.save()

    user.events.append(event)

    fridge = fridge_collection.Fridge.find_one()  # todo is this fine?
    for item, quantity in transactions.items():
        fridge.transact_item(item, quantity)

    return jsonify(event=event.to_json())


@events_blueprint.route("/", methods=["GET"])
def get_events():
    events = event_collection.Event.find()
    return jsonify(events=[event.to_json() for event in events])

@events_blueprint.route("/<event_id>", methods=["GET"])
def get_event(event_id):
    event = event_collection.Event.get_from_id(event_id)

    return jsonify(event=event.to_json())