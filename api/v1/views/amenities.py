#!/usr/bin/python3
"""
module: State api
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.amenity import Amenity
from models import storage


@app_views.route('/amenities/', methods=['GET'], strict_slashes=False)
def get_amenities():
    """ returns all amenities """
    _amenities = [amenity.to_json()
                  for amenity in storage.all('Amenity').values()]
    return jsonify(_amenities)


@app_views.route('/amenities/<string:amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenities_byID(amenity_id=None):
    """ returns amenity by id """
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    return(jsonify(amenity.to_json()))


@app_views.route('/amenities/<string:amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenities_byID(amenity_id=None):
    """ delete amenity by id"""
    amenity = storage.get("Amenity", amenity_id)
    if not amenity:
        abort(404)
    storage.delete(amenity)
    return jsonify({})


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def post_amenity():
    """ creates an amenity  """
    json_obj = None
    try:
        json_obj = request.get_json()
    except:
        return 'Not a JSON', 400

    if 'name' not in json_obj.keys():
        return 'Missing name', 400
    amenity = Amenity(**json_obj)
    amenity.save()
    return jsonify(amenity.to_json()), 201


@app_views.route('/amenities/<string:amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def put_amenities_byID(amenity_id=None):
    """ update an amenityby id"""
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    try:
        request_data = request.get_json()
    except:
        request_data = None
    if request_data is None:
        return "Not a JSON", 404
    for item in ("id", "created_at", "updated_at"):
        request_data.pop(item, None)
    for k, v in request_data.items():
        setattr(amenity, k, v)
    amenity.save()
    return jsonify(amenity.to_json()), 200
