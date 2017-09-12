#!/usr/bin/python3
from flask import Blueprint

app_views = Blueprint('app_views', __name__, template_folder='/api/v1')

@app_views.route('/status/')
def status():
    return "{status: OK}"
