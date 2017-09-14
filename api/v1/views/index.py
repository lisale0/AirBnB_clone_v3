#!/usr/bin/python3
"""
Module: index
"""
from api.v1.views import app_views
from flask import jsonify
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


@app_views.route('/status/', strict_slashes=False)
def status():
    """ returns status: OK JSON  """
    return jsonify({"status": "OK"})


#@app_views.route('/stats/', strict_slashes=False)
#def stats():
#    """ returns count: all models  """
#    cls_models = {"amenities": "Amenity", "cities": "City",
#                  "places": "Place", "reviews": "Review",
#                  "states": "State", "users": "User"}
#    ret_count = {}
#    for k, v in cls_models.items():
#        if storage.count(v):
#            ret_count[k] = storage.count(v)
#        else:
#            ret_count[k] = 0
#    return jsonify(ret_count)

@app_views.route('/stats/', strict_slashes=False)
def stats():
    """ returns number of objects by type  """
    class_counts = {}
    convert_dict = {
        'Amenity': 'amenity',
        'State': 'state',
        'City': 'city',
        'User': 'user',
        'Place': 'place',
        'Review': 'review'
    }

    for k, v in convert_dict.items():
        class_counts[v] = storage.count(k)

    return jsonify(class_counts)
