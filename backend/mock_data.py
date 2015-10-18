__author__ = 'Felix'

import requests
import json
from settings import port
host = 'localhost'
port = str(port)

user1 = {"username": "Bene", "device": "C2:71:93:D3:2D:61"}
user2 = {"username": "Philipp", "device": "D2:7A:9D:34:2D:2D"}
user3 = {"username": "Felix", "device": "D2:7A:9D:34:2A:2D"}
requests.post("http://" + host + ":" + port + "/users/", data = json.dumps(user1))
requests.post("http://" + host + ":" + port + "/users/", data = json.dumps(user2))
requests.post("http://" + host + ":" + port + "/users/", data = json.dumps(user3))

event1 = {"username": "Bene", "transactions": {"Beer": 20, "Water": 10, "Lemonade": 2, "Jagermeister": 3}}
event2 = {"username": "Felix", "transactions": {"Beer": -1}}
event3 = {"username": "Bene", "transactions": {"Beer": -3}}
event4 = {"username": "Philipp", "transactions": {"Beer": -5, "Water": -1, "Vodka": 1}}
event5 = {"username": "Philipp", "transactions": {"Lemonade": -1}}
event6 = {"username": "Bene", "transactions": {"Water": -1, "Spezi": 1}}
event7 = {"username": "Felix", "transactions": {"Beer": -5, "Water": -2, "Coke": 2}}
event8 = {"username": "Bene", "transactions": {"Beer": -6}}
event9 = {"username": "Felix", "transactions": {"Beer": 20, "Water": 4, "Lemonade": 2, "Juice": 1}}
event10 = {"username": "Philipp", "transactions": {"Beer": -20, "Vodka": -1, "Coke": -2, "Lemonade": -3}}
event11 = {"username": "Bene", "transactions": {"Jagermeister": -3, "Water": -10, "Juice": -1}}


for i in xrange(11):
    requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event1))
    requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event2))
    requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event3))
    requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event4))
    requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event5))
    requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event6))
    requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event7))
    requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event8))
    requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event9))
    requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event10))
    requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event11))


requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event1))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event2))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event3))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event4))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event5))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event6))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event7))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event8))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event9))