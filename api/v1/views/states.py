#!/usr/bin/python3
"""
Module: index
"""
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models.base_model import BaseModel
from models.state import State
from models import storage


@app_views.route('/states/', methods=['GET'], strict_slashes=False)
def get_all_states():
    """ returns all state objects in JSON format   """
    _states = [state.to_json() for state in storage.all('State').values()]
    return jsonify(_states)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state_byID(state_id=None):
    """ returns a state object in JSON format  """
    if state_id:
        state = storage.get('State', state_id)
        if state:
            return jsonify(state.to_json())
    abort(404)


@app_views.route('/states/<string:state_id>/',
                 strict_slashes=False, methods=['DELETE'])
def delete_state_byID(state_id):
    """ delete state by id"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    return jsonify({}), 200


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


@app_views.route('/states/<string:state_id>/',
                 strict_slashes=False, methods=['PUT'])
def put_state_byID(state_id):
    """ update a state by id"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    try:
        request_data = request.get_json()
    except:
        request_data = None
    if request_data is None:
        return "Not a JSON", 404
    if 'id' in request_data.keys():
        request_data.pop('id')
    if 'created_at' in request_data.keys():
        request_data.pop('created_at')
    if 'updated_at' in request_data.keys():
        request_data.pop('updated_at')
    for k, v in request_data.items():
        setattr(state, k, v)
    state.save()
    return jsonify(state.to_json()), 200
