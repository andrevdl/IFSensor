from flask.views import MethodView

class ManageAPI(MethodView):
    def get(self, action):
        return {"action": action}