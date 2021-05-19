import os

from flask import Flask
from flask import jsonify, request

from datetime import datetime

from . import utils, db, system, security
from .api import rest_api, auth
from .views import views
import IFSensor.model.user

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.db.init_app(app)
    security.jwt.init_app(app)
    
    security.password_system.init_app(app)

    @app.errorhandler(404)
    @app.errorhandler(405)
    def _handle_api_error(ex):
        if request.path.startswith('/api/'):
            return jsonify(error=str(ex))
        else:
            return ex

    # A test method to check if the server still response
    @app.route('/alive')
    def alive():
        return {"datetime": datetime.now()}

    app.register_blueprint(system.setup_path)
    app.register_blueprint(auth)
    app.register_blueprint(views)                
    app.register_blueprint(rest_api)                   

    return app