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


@app_views.route('/states/<string:state_id>/cities', strict_slashes=False)
def get_amenities_byState(state_id):
    """ returns cities: return all cities from
    specified state in json format  """
    all_cities = storage.all("City")
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    json_array = []
    for k, v in all_cities.items():
        if (v.to_json()['state_id'] == state_id):
            json_array.append(v.to_json())
    return (jsonify(json_array))


@app_views.route('/cities/<string:city_id>',
                 strict_slashes=False, methods=['GET'])
def get_amenities_byID(city_id):
    """ returns state by id """
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    return(jsonify(city.to_json()))


@app_views.route('/cities/<string:city_id>/',
                 strict_slashes=False, methods=['DELETE'])
def delete_amenities_byID(city_id):
    """ delete state by id"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    return jsonify({}), 200


@app_views.route('/cities/<string:city_id>/',
                 strict_slashes=False, methods=['PUT'])
def put_amenities_byID(city_id):
    """ update a state by id"""
    city = storage.get("City", city_id)
    if city is None:
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
        setattr(city, k, v)
    city.save()
    return jsonify(city.to_json()), 200
