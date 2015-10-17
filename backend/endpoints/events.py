__author__ = 'dowling'
from flask import request, Blueprint, jsonify
from model.db import db
from model.event import Event
import datetime
events_blueprint = Blueprint("events", __name__, url_prefix="/events")

fridge_collection = db.fridges
event_collection = db.events

@events_blueprint.route("/", methods=["POST"])
def post_event():
    data = request.get_json(force=True)
    # TODO read data from json (what was taken/added, who did it, etc)
    event = event_collection.Event()
    event.user = data["user"]
    event.timestamp = datetime.datetime.now()

    transactions = data["transactions"]
    event.transactions = transactions
    event.save()

    fridge = fridge_collection.Fridge.find_one()  # todo is this fine?
    for item, quantity in transactions.items():
        fridge.transact_item(item, quantity)



    return


@events_blueprint.route("/", methods=["GET"])
def get_events():
    events = event_collection.Event.find()
    return jsonify(events=[event.to_json() for event in events])

@events_blueprint.route("/<event_id>", methods=["GET"])
def get_event(event_id):
    event = event_collection.Event.find_one() # TODO find by id

    return