from flask import Blueprint, request
from models.users import fetch
from flask import jsonify


blueprint  = Blueprint("user", __name__)

@blueprint.route('/users', methods=("GET", ))
def register():
    users = fetch(1, 2, name="kofi")
    return jsonify(users)