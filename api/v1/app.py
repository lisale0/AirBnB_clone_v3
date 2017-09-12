#!/usr/bin/python3
"""
Module: app
"""
from flask import Flask
from api.v1.views import app_views
from models import storage
from os import getenv
from flask import jsonify

app = Flask(__name__)
app.register_blueprint(app_views)

@app.errorhandler(404)
def notFound(error):
    """ return 404"""
    return jsonify({"error": "Not found"}), 404

@app.teardown_appcontext
def teardown(self):
    """ close storage session """
    storage.close()

if __name__ == "__main__":
    _host = getenv('HBNB_API_HOST', '0.0.0.0')
    _port = getenv('HBNB_API_PORT', 5000)
    app.run(host=_host, port=_port)
