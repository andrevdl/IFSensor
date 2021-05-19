from flask.views import MethodView
from flask_jwt_extended import jwt_required

class SensorAPI(MethodView):
    @jwt_required()
    def get(self, sensor_id):
        return {"id": sensor_id, "name": "Binnen sensor #1", "sensor_type": "DHT22", "port": 4, "import_interval": 2, "export_interval": 10000, "sensor_group": {"id": 2, "name": "Kas", "group": {"id": 24, "name": "Binnen"}}}

    @jwt_required()
    def post(self):
        return {"ok": True}