from flask_jwt_extended import current_user

class ViewController:
    def get_message(self):
        return ''
    def get_ok(self):
        return ''
    def get_warning(self):
        return ''
    def get_error(self):
        return '' 
    def is_logged_in(self):
        return current_user != None
    def username(self):
        return current_user.username

view_controller = ViewController()