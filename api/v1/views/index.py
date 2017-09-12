#!/usr/bin/python3
"""
Module: index
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status/', strict_slashes=False)
def status():
    """ returns status: OK JSON  """
    return jsonify({"status": "OK"})


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
