from flask.views import MethodView

class DeviceGroupAPI(MethodView):
    def get(self, id):
        return {"id": id, "group": {"id": 24, "name": "Binnen"}}