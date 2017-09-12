#!/usr/bin/python3
from api.v1.views import app_views
from flask import Blueprint
from flask import Flask

app = Flask(__name__)

@app.route('/status')
def status(app_views):
    
