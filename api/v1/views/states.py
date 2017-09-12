#!/usr/bin/python3
"""
module: State api
"""
from api.v1.views import app_views
from flask import jsonify
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.amenity import Amenity
from models import storage

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
    all_states = storage.all("State")
    for k, v in all_states.items():
        if k == state_id:
            return(jsonify(v.to_json()))
