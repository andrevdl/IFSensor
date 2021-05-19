from flask import Blueprint, request
from IFSensor.utils import register_api, CRUDMethods

from .v1 import sensor, sensor_group, sensor_group_raw_data, sensor_group_data, group, manage, setting, user, command, device, timer, device_type, device_group, condition, measure

# todo: move to own file, handles auth
from IFSensor.utils import validate_json
from IFSensor.model.user import User
from flask import render_template, make_response, redirect
from flask_jwt_extended import jwt_required

rest_api = Blueprint('rest_api', __name__, url_prefix='/api/v1')

# Sensors
register_api(rest_api, CRUDMethods.ALL, sensor.SensorAPI,
             'sensor_api', '/sensor/', pk='sensor_id')
register_api(rest_api, CRUDMethods.ALL, sensor_group.SensorGroupAPI,
             'sensor_group_api', '/sensor/group/', pk='group_id')
register_api(rest_api, CRUDMethods.READ, sensor_group_raw_data.SensorGroupRawDataAPI,
             'sensor_group_raw_data_api', '/sensor/group/<int:group_id>/raw/', pk='data_id')
register_api(rest_api, CRUDMethods.READ, sensor_group_data.SensorGroupDataAPI,
             'sensor_group_data_api', '/sensor/group/<int:group_id>/data/', pk='data_id')
register_api(rest_api, CRUDMethods.SEARCH_WITHOUT_ID, sensor_group_data.SensorGroupRangeAPI,
             'sensor_group_range_api', '/sensor/group/<int:group_id>/range/<int:from_datetime>/<int:to_datetime>/')

# Devices
register_api(rest_api, CRUDMethods.ALL, device.DeviceAPI,
             'device_api', '/device/')
register_api(rest_api, CRUDMethods.ALL, device_group.DeviceGroupAPI,
             'device_group_api', '/device/group/')
register_api(rest_api, CRUDMethods.ALL, device_type.DeviceTypeAPI,
             'device_type_api', '/device/type/')
register_api(rest_api, CRUDMethods.ALL, command.CommandAPI,
             'command_api', '/command/')

# General
register_api(rest_api, CRUDMethods.ALL,
             group.GroupAPI, 'group_api', '/group/', pk='group_id')
register_api(rest_api, CRUDMethods.ALL, condition.ConditionAPI,
             'condition_api', '/condition/')
register_api(rest_api, CRUDMethods.ALL, timer.TimerAPI,
             'timer_api', '/timer/')

# Management
register_api(rest_api, CRUDMethods.ALL, user.UserAPI,
             'user_api', '/user/')
register_api(rest_api, CRUDMethods.ALL, measure.MeasureAPI,
             'measure_api', '/measure/')
register_api(rest_api, CRUDMethods.GET_EXECUTE, manage.ManageAPI,
             'manage_api', '/manage/', pk='action', pk_type='string')
register_api(rest_api, CRUDMethods.ALL, setting.SettingAPI,
             'setting_api', '/setting/', pk='id')

auth = Blueprint('auth', __name__)

@auth.route('/auth/tokens/', methods=["POST"])
@validate_json
def get_tokens():
    username = request.json.get('username', None)
    password = request.json.get("password", None)
    return User.get_tokens(username, password)     

@auth.route('/auth/refresh/', methods=["POST"])
@jwt_required(refresh=True)
def refresh_tokens():
    return User.refresh_tokens()

@auth.route('/login/', methods=["POST"])
def login():
    response = make_response(redirect('/'))
    if (User.get_tokens(request.form.get('username', ''), request.form.get('password', ''), True, response)):
        return response
         
    response = make_response(render_template('login.html', is_wrong=True))    
    User.delete_tokens(response)

    return response

@auth.route('/login/', methods=["GET"])
def login2():
    return render_template('login.html', password=23)
