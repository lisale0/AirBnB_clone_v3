from flask import Blueprint
from api import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
