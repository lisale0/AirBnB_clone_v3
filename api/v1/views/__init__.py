#!/usr/bin/python3
"""
Module: __init__ - initializes the views folder
"""
# order matters: the Blueprint instance must be defined
# before importing everything from index

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
