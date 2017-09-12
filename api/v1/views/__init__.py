from flask import Blueprint
from api import *

app_views = Blueprint('app_views', __name__, template_folder='/api/v1')
