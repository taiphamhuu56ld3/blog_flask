
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_dance.contrib.github import github, make_github_blueprint
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "b2dd17eb994d430edbc07467c6805875"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category ='info'

blueprint = make_github_blueprint(
    client_id="Ov23liCBryBDxvtnwTqH",
    client_secret="0f23236da39e20bd27b6669d12c4808d75b44c7f",
)
app.register_blueprint(blueprint, url_prefix="/login")

from flaskblog import routes
