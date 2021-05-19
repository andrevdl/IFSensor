from IFSensor.db import db
from IFSensor.security import password_system, jwt

from flask import jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, set_access_cookies, current_user, unset_jwt_cookies

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password not readable')

    @password.setter
    def password(self, plaintext):
        self.password_hash = password_system.generate_password_hash(plaintext)

    def verify_password(self, password):
        return password_system.check_password_hash(self.password_hash, password)

    @staticmethod
    def create_tokens(identity, fresh):
        access_token = create_access_token(identity=identity, fresh=fresh)
        refresh_token = create_refresh_token(identity=identity)    
        return access_token, refresh_token

    @staticmethod
    def get_tokens(username, password, web=False, response=None):
        user = User.query.filter_by(username=username).one_or_none()

        if user and user.verify_password(password):
            access_token, refresh_token = User.create_tokens(user, True)    

            if web:
                set_access_cookies(response, access_token)
                return True
            else:
               return jsonify(access_token=access_token, refresh_token=refresh_token) 
        else:
            if web:
                return False
            else:
                return jsonify("Invalid username or password"), 401
    
    @staticmethod
    def delete_tokens(response):
        unset_jwt_cookies(response)
        pass

    @staticmethod
    def refresh_tokens():
        identity = get_jwt_identity()
        return User.create_api_tokens(identity, False)

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"] # get_jwt_identity()
    return User.query.filter_by(id=identity).one_or_none()    

# class RefreshToken(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.String(128))
#     token = db.Column(db.String(128))