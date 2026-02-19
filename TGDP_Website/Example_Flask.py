import os
import flask
from flask import Flask
import json

app = Flask(__name__, instance_relative_config = True)
"""
@app.route("/")
def create_app(test_config = None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY = "password",
        DATABASE = os.path.join(app.instance_path, "flaskr.sqlite")
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent = True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    os.makedirs(app.instance_path, exist_ok = True)
    @app.route("/hello")
    def hello():
        return "Hello World!!!"
    return app
"""
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!!!"

@app.route("/")
def index():
    return "homepage"

@app.route("/game/<diplomacy_game_number>")
def show_diplomacy_game(diplomacy_game_number):
    return f"Here is {diplomacy_game_number}!"

@app.route("/example_json_data", methods = ["GET"])
def users():
    print("owners endpoint reached")
    with open("example_json_data.json", "r") as file_input:
        data = json.load(file_input)
        data.append({
            "owner": "Nicola",
            "pets": ["Mango"]
        })
        return flask.jsonify(data)

# runs if I use http://127.0.0.1:5000/hello
if __name__ == "__main__":
    app.run(debug = True)

