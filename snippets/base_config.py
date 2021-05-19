from datetime import timedelta

SQLALCHEMY_DATABASE_URI = "sqlite:///../instance/IFSensor.sqlite"
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_SECRET_KEY = "super-secret"  # Change this!
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)