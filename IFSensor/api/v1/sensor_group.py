from flask.views import MethodView

class SensorGroupAPI(MethodView):
    def get(self, group_id):
        return {"id": group_id, "name": "Kas", "store_interval": 60, "group": {"id": 24, "name": "Binnen"}}