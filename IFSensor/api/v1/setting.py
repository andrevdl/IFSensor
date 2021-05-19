from flask.views import MethodView

class SettingAPI(MethodView):
    def get(self, id):
        return {"id": id, "name": "Setting", "int_value": 0, "string_value": "", "type": 1}