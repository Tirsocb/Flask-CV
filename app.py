# FLASK
from flask import Flask, jsonify, render_template, request
import os, optparse
import yaml

app = Flask(__name__)

developer = os.getenv("DEVELOPER", "Tirso")
environment = os.getenv("ENVIRONMENT", "development")

with open("info.yml", 'r', encoding='utf-8') as stream:
    try:
        info = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


@app.route("/")
def home():
    foo = "bar"
    return render_template("home.html", info=info)


@app.route("/studies")
def studies():
    return render_template("studies.html", info=info['studies'])

@app.route("/experience")
def experience():
    return render_template("experience.html", info=info['experience'])


if __name__ == "__main__":
    debug = False
    if environment == "development" or environment == "local":
        debug = True
    app.run(host="0.0.0.0", debug=debug)
