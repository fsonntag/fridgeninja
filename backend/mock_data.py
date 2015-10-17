__author__ = 'Felix'

import requests
import json
from settings import host, port

port = str(port)

user1 = {"username": "Bene", "device": "Sony Z3"}
user2 = {"username": "Philipp", "device": "OnePlus One"}
user3 = {"username": "Felix", "device": "Xiaomi Mi3"}
requests.post("http://" + host + ":" + port + "/users/", data = json.dumps(user1))
requests.post("http://" + host + ":" + port + "/users/", data = json.dumps(user2))
requests.post("http://" + host + ":" + port + "/users/", data = json.dumps(user3))

event1 = {"username": "Bene", "transactions": {"beer": 20, "water": 10, "lemonade": 2, "Jagermeister": 3}}
event2 = {"username": "Felix", "transactions": {"beer": -1}}
event3 = {"username": "Bene", "transactions": {"beer": -3}}
event4 = {"username": "Philipp", "transactions": {"beer": -5, "water": -1, "vodka": 1}}
event5 = {"username": "Philipp", "transactions": {"lemonade": -1}}
event6 = {"username": "Bene", "transactions": {"water": -1, "Spezi": 1}}
event7 = {"username": "Felix", "transactions": {"beer": -5, "water": -2, "coke": 2}}
event8 = {"username": "Bene", "transactions": {"beer": -6}}
event9 = {"username": "Felix", "transactions": {"beer": 20, "water": 10, "lemonade": 2, "juice": -1}}

requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event1))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event2))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event3))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event4))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event5))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event6))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event7))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event8))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event9))