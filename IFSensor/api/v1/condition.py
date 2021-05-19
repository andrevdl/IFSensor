from flask.views import MethodView

class ConditionAPI(MethodView):
    def get(self, id):
        return {"id": id, "name": "Freezing", "measure": {"id": 1, "name": "temperature"}, "operator": 2, "value_1": 3.5, "value_2": 5.3, "scope": 3}