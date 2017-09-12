#!/usr/bin/python3
from flask import Flask
from api.v1.views import app_views
from models.engine import storage
import os

app = Flask(__name__)


@app.teardown_appcontext
def close_storage():
    """ closes storage """
    storage.close()

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST')
    port = os.getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = 5000

