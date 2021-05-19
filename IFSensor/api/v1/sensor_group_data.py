from flask.views import MethodView

# test
from datetime import datetime

class SensorGroupDataAPI(MethodView):
    def get(self, group_id, data_id):
        return {"id": data_id, "value": 20.3, "interval": 30, "timestamp": datetime.now(), "measure": {"id": 1, "name": "temperature"}, "sensor_group": {"id": 54, "name": "Kas", "group": {"id": 24, "name": "Binnen"}}}

class SensorGroupRangeAPI(MethodView):
    def get(self, group_id, from_datetime, to_datetime):
        return {"id": group_id, "value": 20.3, "interval": 30, "timestamp": datetime.now(), "measure": {"id": 1, "name": "temperature"}, "sensor_group": {"id": 54, "name": "Kas", "group": {"id": 24, "name": "Binnen"}}}        