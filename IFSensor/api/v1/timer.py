from flask.views import MethodView

# test
import time
from datetime import datetime

class TimerAPI(MethodView):
    def get(self, id):
        return {"id": id, "name": "clean-up", "device_group": {"id": id, "group": {"id": 24, "name": "Binnen"}}, "sensor_group": {"id": 23, "name": "Kas", "store_interval": 60, "group": {"id": 24, "name": "Binnen"}}, "interval": 0, "last": datetime.now(), "prio": 1, "exclusive": True, "mode": 4, "handler": "abc.xyz", "conditon": {"id": id, "name": "Freezing", "measure": {"id": 1, "name": "temperature"}, "operator": 2, "value_1": 3.5, "value_2": 5.3, "scope": 3}, "start_time": time.strftime("%H:%M:%S", time.localtime())}