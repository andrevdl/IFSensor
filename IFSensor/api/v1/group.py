from flask.views import MethodView

class GroupAPI(MethodView):
    def get(self, group_id):
        return {"id":  group_id, "name": "Binnen"}