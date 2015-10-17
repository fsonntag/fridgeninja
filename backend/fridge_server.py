__author__ = 'dowling'
import logging
logging.basicConfig(format="%(asctime)s %(levelname)-8s %(name)-18s: %(message)s", level=logging.DEBUG)

from flask import Flask

app = Flask(__name__, static_path="/")
app.config.from_object(__name__)


from endpoints.events import events_blueprint
from endpoints.users import user_blueprint
app.register_blueprint(events_blueprint)
app.register_blueprint(user_blueprint)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)
