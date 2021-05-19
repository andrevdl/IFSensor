from flask.views import MethodView

# test
from datetime import datetime

class SensorGroupRawDataAPI(MethodView):
    def get(self, group_id, data_id):
        return {"id": data_id, "value": 20.3, "interval": 30, "timestamp": datetime.now(), "measure": {"id": 1, "name": "temperature"}, "sensor_group": {"id": group_id, "name": "Kas", "group": {"id": 24, "name": "Binnen"}}}