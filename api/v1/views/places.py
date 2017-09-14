#!/usr/bin/python3
"""
module: Place api
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.city import City


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def get_places_byCityId(city_id=None):
    """ returns all places by city """
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    _places = [place.to_json()
               for place in city.places]
    return jsonify(_places)


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def get_place_byID(place_id=None):
    """ get place by ID """
    if place_id is None:
        abort(404)
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    return(jsonify(place.to_json()))


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_places_byID(place_id=None):
    """ delete place by id"""
    if place_id is None:
        abort(404)
    place = storage.get("Place", place_id)
    if not place:
        abort(404)
    storage.delete(place)
    return jsonify({})


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def post_place(city_id):
    """ creates a place  """
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    json_obj = None
    try:
        json_obj = request.get_json()
    except:
        return 'Not a JSON', 400
    if 'name' not in json_obj.keys():
        return 'Missing name', 400
    if 'user_id' not in json_obj.keys():
        return 'Missing user_id', 400
    user = storage.get("User", user_id)
    if user is None:
        abort(404)
    json_obj["city_id"] = city_id
    place = Place(**json_obj)
    place.save()
    return jsonify(place.to_json()), 201


@app_views.route('/places/<place_id>', methods=['PUT'],
                 strict_slashes=False)
def put_place_byID(place_id=None):
    """ update a place by id"""
    if place_id is None:
        abort(404)
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    try:
        response = request.get_json()
    except:
        response = None
    if response is None:
        return "Not a JSON", 400
    for item in ("id", "created_at", "updated_at"):
        response.pop(item, None)
    for k, v in response.items():
        setattr(place, k, v)
    place.save()
    return jsonify(place.to_json()), 200
