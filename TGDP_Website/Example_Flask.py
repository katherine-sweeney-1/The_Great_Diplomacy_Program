import os
import flask
from flask import Flask, request, render_template
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/hello")
def hello():
    return "Hello World!!!"

@app.route("/")
def index():
    return "homepage"

@app.route("/")
def home():
    europe_map_url = "The_Great_Diplomacy_Program/GUI/Europe_Map.png"
    return render_template("index.html", image_url = europe_map_url)


@app.route("/game/<diplomacy_game_number>")
def show_diplomacy_game(diplomacy_game_number):
    return f"Here is {diplomacy_game_number}!"

@app.route("/example", methods = ["GET", "POST"])
def users():
    print("owners endpoint reached")
    if request.method == "GET":
        with open("TGDP_Website/example_json_data.json", "r") as file_input:
            data = json.load(file_input)
            data.append({
                "owner": "Nicola",
                "pets": ["Mango"]
            })
            return flask.jsonify(data)
    if request.method == "POST":
        received_data = request.get_json()
        print(f"received data: {received_data}")
        message = received_data["data"]
        return_data = {
            "status": "success",
            "message": f"received: {message}"
        }
        return flask.Response(response = json.dumps(return_data), status = 201)


# runs if I use http://127.0.0.1:5000/hello
if __name__ == "__main__":
    app.run("localhost", 5000, debug = True)



"""

run python file first
then run html file

"""