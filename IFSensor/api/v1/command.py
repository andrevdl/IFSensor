from flask.views import MethodView

# test
from datetime import datetime

class CommandAPI(MethodView):
    def get(self, id):
        return {"id": id, "mode": 1, "action": 2, "timestamp": datetime.now(), "device_group": {"id": 45, "group": {"id": 24, "name": "Binnen"}}, "device": {"id": id, "name": "Window #1", "last_change": datetime.now(), "state": 0, "device_group": {"id": 45, "group": {"id": 24, "name": "Binnen"}}, "device_type": {"id": 5, "name": "Window"}}}