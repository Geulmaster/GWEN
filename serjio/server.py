from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "I am Serjio"

@app.route("/paths")
def paths():
    with open(r"data/paths.json", "r") as content:
        info = json.load(content)
    return info

app.run(host="localhost", port=5000, debug=True)
