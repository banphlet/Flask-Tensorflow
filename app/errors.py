from flask import Blueprint, render_template
import os
from lib import cache



blueprint  = Blueprint("error", __name__)


@blueprint.app_errorhandler(404)
@cache.cached(timeout=50)
def error_handler(error):
    return render_template('index.html')