__author__ = 'dowling'
from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)

from endpoints.hello import hello_blueprint
app.register_blueprint(hello_blueprint)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
