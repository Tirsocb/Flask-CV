# FLASK
from flask import Flask, jsonify, render_template, request
import os, optparse

app = Flask(__name__)

developer = os.getenv("DEVELOPER", "Tirso")
environment=os.getenv("ENVIRONMENT", "development")


if __name__ == "__main__":
    debug = False
    if environment == "development" or environment == "local":
        debug = True
    app.run(host="0.0.0.0", debug=debug)
