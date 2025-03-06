# Run file to create database
from flask import current_app

from flaskblog import db
from flaskblog.models import User

with current_app.app_context():
    db.create_all()
