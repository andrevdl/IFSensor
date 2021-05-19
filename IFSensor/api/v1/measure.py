from flask.views import MethodView

class MeasureAPI(MethodView):
    def get(self, id):
        return {"id": id, "name": "temperature"}