from flask import Flask, Blueprint, request, render_template
from config.index import Config
from app import users
from lib.db import db



from .exceptions import ExceptionHandler
from . import blueprint
from lib import cache


def create_app(config_object=Config):
    """ Factory function to start application  """
    app = Flask(__name__.split('.')[0], static_folder='../client/build/static', template_folder="../client/build")

    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    db.init_app(app)
    cache.init_app(app)
    register_blueprints(app)
    register_error_handler(app)
    

    return app


def register_blueprints(app):
    app.register_blueprint(users.routes.blueprint)
    app.register_blueprint(blueprint)


    


def register_error_handler(app):
    """ Register function for handling errors  """
    def errorhandler(error):
        response = error.to_json()
        response.status_code = error.status_code
        print(response.status_code)
        return response

    app.errorhandler(ExceptionHandler)(errorhandler)