#!/usr/bin/python3
"""
module: State api
"""
from api.v1.views import app_views
from flask import jsonify
from flask import abort
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.amenity import Amenity
from models import storage
from flask import request

@app_views.route('/states/', strict_slashes=False)
def get_states():
    """ returns states: return all states in json format  """
    all_states = storage.all("State")
    json_array = []
    for k,v in all_states.items():
        json_array.append(v.to_json())
    return (jsonify(json_array))

@app_views.route('/states/<string:state_id>', strict_slashes=False, methods=['GET'])
def get_state_byID(state_id):
    """ returns state by id """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return(jsonify(state.to_json()))


@app_views.route('/states/<string:state_id>/', strict_slashes=False, methods=['DELETE'])
def delete_state_byID(state_id):
    """ delete state by id"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    return jsonify({}), 200

@app_views.route('/states/<string:state_id>/', strict_slashes=False, methods=['PUT'])
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
