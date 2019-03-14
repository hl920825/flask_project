from flask import Blueprint

cms_bp = Blueprint("cms",__name__)

from . import auth_view