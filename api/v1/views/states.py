#!/usr/bin/python3
"""
Module: index
"""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.state import State
# from models.base_model impoert BaseModel


@app_views.route('/states/', methods=['GET'], strict_slashes=False)
def view_all_states():
    """ returns all state objects in JSON format   """
    _states = [state.to_json() for state in storage.all('State').values()]

    return jsonify(_states)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def view_state(state_id=None):
    """ returns a state object in JSON format  """
    if state_id:
        state = storage.get('State', state_id)
        if state:
            return jsonify(state.to_json())

    abort(404)


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def post_state():
    """ creates a state  """
    json_obj = None
    try:
        json_obj = request.get_json()
    except:
        return 'Not a JSON', 400

    if 'name' not in json_obj.keys():
        return 'Missing name', 400

    state = State(**json_obj)
    state.save()
    return jsonify(state.to_json()), 201
