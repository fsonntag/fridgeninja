__author__ = 'dowling'
import logging
logging.basicConfig(format="%(asctime)s %(levelname)-8s %(name)-18s: %(message)s", level=logging.DEBUG)

from flask import Flask
from settings import host, port

app = Flask(__name__, static_path="/")
app.config.from_object(__name__)


from endpoints.events import events_blueprint
from endpoints.users import user_blueprint
from endpoints.inventory import fridge_blueprint
from endpoints.admin import admin_blueprint
app.register_blueprint(events_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(fridge_blueprint)
app.register_blueprint(admin_blueprint)

if __name__ == "__main__":
    app.run(debug=True, host=host, port=port)
