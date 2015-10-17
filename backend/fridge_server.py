__author__ = 'dowling'
import logging
logging.basicConfig(format="%(asctime)s %(levelname)-8s %(name)-18s: %(message)s", level=logging.DEBUG)

from flask import Flask, send_from_directory

app = Flask(__name__, static_path="/")
app.config.from_object(__name__)

from model.user import User
from model.fridge import Fridge
from model.event import Event


from endpoints.events import events_blueprint
from endpoints.users import user_blueprint
from endpoints.inventory import fridge_blueprint
from endpoints.admin import admin_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(events_blueprint)
app.register_blueprint(fridge_blueprint)
app.register_blueprint(admin_blueprint)

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def server_static(path):
    return send_from_directory('../frontend/', path)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)
