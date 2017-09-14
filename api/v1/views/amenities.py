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

@app_views.route('/amenities/', methods=['GET'], strict_slashes=False)
def get_amenities():
    """ returns all amenities """
    _amenities = [amenity.to_json() for amenity in storage.all('Amenity').values()]
    return jsonify(_amenities)

@app_views.route('/amenities/<string:amenity_id>', strict_slashes=False, methods=['GET'])
def get_amenities_byID(amenity_id):
    """ returns amenity by id """
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    return(jsonify(amenity.to_json()))

@app_views.route('/amenities/<string:amenity_id>', strict_slashes=False, methods=['DELETE'])
def delete_amenities_byID(amenity_id):
    """ delete amenity by id"""
    amenity = storage.get("Amenity", amenity_id)
    if not amenity:
        abort(404)
    storage.delete(amenity)
    return jsonify({}), 200

@app_views.route('/cities/<string:city_id>/', strict_slashes=False, methods=['PUT'])
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
