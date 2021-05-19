from flask.views import MethodView

class DeviceTypeAPI(MethodView):
    def get(self, id):
        return {"id": id, "name": "Window"}