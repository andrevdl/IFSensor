from flask.views import MethodView

class UserAPI(MethodView):
    def get(self, id):
        return {"id": id, "username": "Jan"}