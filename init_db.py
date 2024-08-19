# Run file to create database
from flaskblog import db, app
from flaskblog.models import User

with app.app_context():
    db.create_all()
