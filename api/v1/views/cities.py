#!/usr/bin/python3
"""
module: State api
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.state import State
from models.city import City
from models import storage


@app_views.route('/states/<string:state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities_byState(state_id=None):
    """ returns cities: return all cities
    from specified city in json format  """
    if state_id is None:
        abort(404)
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    else:
        cities = [city.to_json() for city in state.cities]
    return jsonify(cities)


@app_views.route('/cities/<string:city_id>', methods=['GET'],
                 strict_slashes=False)
def get_cities_byID(city_id=None):
    """ returns city by id """
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    return(jsonify(city.to_json()))


@app_views.route('/cities/<string:city_id>/', methods=['DELETE'],
                 strict_slashes=False)
def delete_city_byID(city_id=None):
    """ delete city by id"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', strict_slashes=False,
                 methods=['POST'])
def post_city(state_id):
    """ creates a city  """
    if state_id is None:
        abort(404)
    json_obj = None
    try:
        json_obj = request.get_json()
    except:
        return "Not a JSON", 400
    if 'name' not in json_obj.keys():
        return "Missing name", 400
    json_obj["state_id"] = state_id
    city = City(**json_obj)
    city.save()
    return jsonify(city.to_json()), 201


@app_views.route('/cities/<string:city_id>/', methods=['PUT'],
                 strict_slashes=False)
def put_city_byID(city_id=None):
    """ update a state by id"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    try:
        request_data = request.get_json()
    except:
        request_data = None
    if request_data is None:
        return "Not a JSON", 400
    for item in ("id", "created_at", "updated_at"):
        request_data.pop(item, None)
    for k, v in request_data.items():
        setattr(city, k, v)
    city.save()
    return jsonify(city.to_json()), 200
