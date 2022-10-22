from flask import Blueprint

bp = Blueprint('main', __name__)

import api.routes  # noqa