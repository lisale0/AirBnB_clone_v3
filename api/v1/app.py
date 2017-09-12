#!/usr/bin/python3
from flask import Flask
from views import app_views

import os

app = Flask(__name__)


app.register_blueprint(app_views)

"""
@app.teardown_appcontext
def close_storage():
    storage.close()
"""
if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST')
    port = os.getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = 5000

    app.run(host=host, port=7000)
