from flask import Blueprint, render_template

from .db import db
from .model.user import User
from .model.group import Group

from .security import generate_password, password_system

setup_path = Blueprint('setup_path', __name__)

@setup_path.route('/setup')
def setup():
    # WARNING: only for now => hint the user
    db.drop_all()

    db.create_all()

    password = password=generate_password(16)

    admin = User(username='Admin', password=password)
    db.session.add(admin)

    default_group = Group(name="Default")
    db.session.add(default_group)

    db.session.commit()

    return render_template("setup.html", username="Admin", password=password)