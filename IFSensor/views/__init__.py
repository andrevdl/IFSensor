from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required
from IFSensor.views.view_controller import view_controller

views = Blueprint('views', __name__)

@views.route('/')
@jwt_required(optional=True, locations=["headers", "cookies"])
def home():
    return render_template('home.html', controller=view_controller)

@views.route('/system/')
@jwt_required(optional=True, locations=["headers", "cookies"])
def control_panel():
    return render_template('control-panel.html', controller=view_controller)    