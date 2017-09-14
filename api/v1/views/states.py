#!/usr/bin/python3
"""
Module: index
"""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models.state import State
from models import storage


@app_views.route('/states/', strict_slashes=False, methods=['GET'])
def get_all_states():
    """ returns all state objects in JSON format   """
    _states = [state.to_json() for state in storage.all('State').values()]
    return jsonify(_states)


@app_views.route('/states/<state_id>', strict_slashes=False, methods=['GET'])
def get_state_byID(state_id=None):
    """ returns a state object in JSON format  """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return(jsonify(state.to_json()))


@app_views.route('/states/<string:state_id>/',
                 strict_slashes=False, methods=['DELETE'])
def delete_state_byID(state_id=None):
    """ delete state by id"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.reload()
    return jsonify({}), 200


@app_views.route('/states/', strict_slashes=False, methods=['POST'])
def post_state():
    """ creates a state  """
    json_obj = None
    try:
        json_obj = request.get_json()
    except:
        return "Not a JSON", 400

    if 'name' not in json_obj.keys():
        return "Missing name", 400
    state = State(**json_obj)
    state.save()
    return jsonify(state.to_json()), 201


@app_views.route('/states/<string:state_id>/',
                 strict_slashes=False, methods=['PUT'])
def put_state_byID(state_id=None):
    """ update a state by id"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    try:
        request_data = request.get_json()
    except:
        request_data = None
    if request_data is None:
        return "Not a JSON", 400
    for item in ["id", "created_at", "updated_at"]:
        request_data.pop(item, None)
    for k, v in request_data.items():
        setattr(state, k, v)
    state.save()
    return jsonify(state.to_json()), 200
