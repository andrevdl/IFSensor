import random
import string

from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

password_system = Bcrypt()
jwt = JWTManager()

def generate_password(size, chars = None):
    if chars == None:
        chars = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.choice(chars) for i in range(size))