#!/usr/bin/python3
"""
module: City api
"""
from api.v1.views import app_views, City, storage
from flask import jsonify, abort, request  # from models.state import State


@app_views.route('/states/<string:state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities_byState(state_id):  # <--- removed =None
    """ returns cities: return all cities
    from specified city in json format  """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    cities = [city.to_json() for city in state.cities]
    return jsonify(cities)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_cities_byID(city_id):  # <--- removed '=None', ^removed 'string:'
    """ returns city by id """
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    return(jsonify(city.to_json()))


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city_byID(city_id):  # <--- removed '=None', ^removed'string:'
    """ delete city by id"""
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    return jsonify({})


# this passed
# @app_views.route('/states/<state_id>/cities', methods=['POST'],
#                 strict_slashes=False)
# def post_city(state_id):
#   """ creates a city  """
#   try:
#       response = request.get_json()
#   except:
#       response = None
#
#    if response is None:
#        return "Not a JSON", 400
#    if 'name' not in response.keys():
#        return 'Missing name', 400
#
#    state = storage.get("State", state_id)
#    if state is None:
#        abort(404)
#
#    city = City(**response)
#    city.state_id = state_id
#    city.save()
#    return jsonify(city.to_json()), 201

@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def post_city(state_id=None):
    """ creates a city  """
#    if state_id is None:  # <--- testing
#        abort(404)  # testing
#    state = storage.get("State", state_id)  # <--- testing
#    if state is None:  # <--- testing
#        abort(404)  # testing

    try:
        response = request.get_json()
    except:
        return "Not a JSON", 400
#        response = None  #<--- testing

#    if response is None:  #<--- testing
#        return "Not a JSON", 400  # testing
    if 'name' not in response.keys():
        return 'Missing name', 400

    state = storage.get("State", state_id)  #<-- testing
    if state is None:
        abort(404)

    city = City(**response)
    city.state_id = state_id
    city.save()
    return jsonify(city.to_json()), 201


# this is old post_city

#    if state_id is None:
#        abort(404)
#    state = storage.get("State", state_id)
#    if state is None:
#        abort(404)
#    json_obj = None
#    try:
#        json_obj = request.get_json()
#    except:
#        return "Not a JSON", 400
#    if 'name' not in json_obj.keys():
#        return "Missing name", 400
#    json_obj["state_id"] = state_id
#    city = City(**json_obj)
#    city.save()
#    return jsonify(city.to_json()), 201


@app_views.route('/cities/<city_id>/', methods=['PUT'], strict_slashes=False)
def put_city_byID(city_id):  # <--- removed '=None', ^removed 'string:'
    """ update a state by id """
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    try:
        response = request.get_json()
    except:
        response = None

    if response is None:
        return "Not a JSON", 400
    for item in ("id", "created_at", "updated_at", "state_id"):
        response.pop(item, None)
    for k, v in response.items():
        setattr(city, k, v)
    city.save()
    return jsonify(city.to_json()), 200
