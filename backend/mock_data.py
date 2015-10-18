__author__ = 'Felix'

import requests
import json
from settings import port
import time
import datetime

host = 'localhost'
port = str(port)

user1 = {"username": "Bene", "device": "C2:71:93:D3:2D:61"}
user2 = {"username": "Philipp", "device": "D2:7A:9D:34:2D:2D"}
user3 = {"username": "Felix", "device": "D2:7A:9D:34:2A:2D"}
requests.post("http://" + host + ":" + port + "/users/", data = json.dumps(user1))
requests.post("http://" + host + ":" + port + "/users/", data = json.dumps(user2))
requests.post("http://" + host + ":" + port + "/users/", data = json.dumps(user3))

current_timestamp = time.time()
timestamp1 = current_timestamp - datetime.timedelta(days = 4 * 12).total_seconds()
timestamp2 = timestamp1 + datetime.timedelta(hours = 1).total_seconds()
timestamp3 = timestamp2 + datetime.timedelta(days = 1, hours = 1).total_seconds()
timestamp4 = timestamp3 + datetime.timedelta(minutes = 24).total_seconds()
timestamp5 = timestamp4 + datetime.timedelta(days = 1).total_seconds()
timestamp6 = timestamp5 + datetime.timedelta(hours = 22).total_seconds()
timestamp7 = timestamp6 + datetime.timedelta(minutes = 22).total_seconds()
timestamp8 = timestamp7 + datetime.timedelta(minutes = 33).total_seconds()
timestamp9 = timestamp8 + datetime.timedelta(minutes = 10).total_seconds()
timestamp10 = timestamp9 + datetime.timedelta(hours = 1).total_seconds()
timestamp11 = current_timestamp - datetime.timedelta(days = 4 * 11).total_seconds()



event1 = {"username": "Bene", "transactions": {"Beer": 20, "Water": 10, "Lemonade": 2, "Jagermeister": 3}, "timestamp": timestamp1}
event2 = {"username": "Felix", "transactions": {"Beer": -1}, "timestamp": timestamp2}
event3 = {"username": "Bene", "transactions": {"Beer": -3}, "timestamp": timestamp3}
event4 = {"username": "Philipp", "transactions": {"Beer": -5, "Water": -1, "Vodka": 1}, "timestamp": timestamp4}
event5 = {"username": "Philipp", "transactions": {"Lemonade": -1}, "timestamp": timestamp5}
event6 = {"username": "Bene", "transactions": {"Water": -1, "Spezi": 1}, "timestamp": timestamp6}
event7 = {"username": "Felix", "transactions": {"Beer": -5, "Water": -2, "Coke": 2}, "timestamp": timestamp7}
event8 = {"username": "Bene", "transactions": {"Beer": -6}, "timestamp": timestamp8}
event9 = {"username": "Felix", "transactions": {"Beer": 20, "Water": 4, "Lemonade": 2, "Juice": 1}, "timestamp": timestamp9}
event10 = {"username": "Philipp", "transactions": {"Beer": -20, "Vodka": -1, "Coke": -2, "Lemonade": -3}, "timestamp": timestamp10}
event11 = {"username": "Bene", "transactions": {"Jagermeister": -3, "Water": -10, "Juice": -1}, "timestamp": timestamp11}


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

    timestamp1 = current_timestamp - datetime.timedelta(days = 4 * (11 - i)).total_seconds()
    timestamp2 = timestamp1 + datetime.timedelta(hours = 1).total_seconds()
    timestamp3 = timestamp2 + datetime.timedelta(days = 1, hours = 1).total_seconds()
    timestamp4 = timestamp3 + datetime.timedelta(minutes = 24).total_seconds()
    timestamp5 = timestamp4 + datetime.timedelta(days = 1).total_seconds()
    timestamp6 = timestamp5 + datetime.timedelta(hours = 22).total_seconds()
    timestamp7 = timestamp6 + datetime.timedelta(minutes = 22).total_seconds()
    timestamp8 = timestamp7 + datetime.timedelta(minutes = 33).total_seconds()
    timestamp9 = timestamp8 + datetime.timedelta(minutes = 10).total_seconds()
    timestamp10 = timestamp9 + datetime.timedelta(hours = 1).total_seconds()
    timestamp11 = current_timestamp - datetime.timedelta(days = 4 * (10 - i)).total_seconds()

    event1["timestamp"] = timestamp1
    event2["timestamp"] = timestamp2
    event3["timestamp"] = timestamp3
    event4["timestamp"] = timestamp4
    event5["timestamp"] = timestamp5
    event6["timestamp"] = timestamp6
    event7["timestamp"] = timestamp7
    event8["timestamp"] = timestamp8
    event9["timestamp"] = timestamp9
    event10["timestamp"] = timestamp10
    event11["timestamp"] = timestamp11


event8["timestamp"] = time.time() - datetime.timedelta(hours = 2, minutes = 33).total_seconds()
event9["timestamp"] = time.time() - datetime.timedelta(hours = 2).total_seconds()
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event1))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event2))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event3))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event4))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event5))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event6))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event7))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event8))
requests.post("http://" + host + ":" + port + "/events/", data = json.dumps(event9))