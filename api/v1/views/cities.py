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
    from specified state in json format  """
    if state_id is None:
        abort(404)
    all_cities = storage.all("City")
    state = storage.get("State", state_id)
    if state is None or all_cities is None:
        abort(404)
    json_array = []
    for k, v in all_cities.items():
        if (v.to_json()['state_id'] == state_id):
            json_array.append(v.to_json())
    return (jsonify(json_array))


@app_views.route('/cities/<string:city_id>', methods=['GET'],
                 strict_slashes=False)
def get_cities_byID(city_id=None):
    """ returns state by id """
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    return(jsonify(city.to_json()))


@app_views.route('/cities/<string:city_id>/', methods=['DELETE'],
                 strict_slashes=False)
def delete_city_byID(city_id=None):
    """ delete state by id"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    return jsonify({}), 200


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
    for item in ["id", "created_at", "updated_at"]:
        request_data.pop(item, None)
    for k, v in request_data.items():
        setattr(city, k, v)
    city.save()
    return jsonify(city.to_json()), 200
