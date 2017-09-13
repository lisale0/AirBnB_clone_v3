#!/usr/bin/python3
"""
Module: index
"""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.state import State
from models.base_model import BaseModel


@app_views.route('/states/<string:state_id>', methods=['GET'], strict_slashes=False)
def view_one_state(state_id=None):
    """ returns a state object in JSON format  """
    if state_id is None:
        abort(404)
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_json())
