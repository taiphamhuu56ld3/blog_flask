from flask import Flask
from flask_bcrypt import Bcrypt
from flask_dance.contrib.github import make_github_blueprint
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

from flaskblog.config import Config

app = Flask(__name__)

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category ='info'
mail = Mail()

def create_app(config_class=Config):
    app.config.from_object(config_class)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    from flaskblog import routes
    blueprint = make_github_blueprint(
        client_id="Ov23liCBryBDxvtnwTqH",
        client_secret="0f23236da39e20bd27b6669d12c4808d75b44c7f",
    )
    app.register_blueprint(blueprint, url_prefix="/login")
    return app
