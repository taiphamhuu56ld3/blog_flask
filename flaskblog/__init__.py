import os

from dotenv import load_dotenv
from flask import Flask
from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_dance.contrib.github import make_github_blueprint
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flaskblog.config import Config
from flaskblog.utils import Status


load_dotenv()

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_database(app: Flask):
    with app.app_context():
        db_path = app.config["SQLALCHEMY_DATABASE_URI"].replace(
            "sqlite:///", "")
        if not os.path.exists(db_path):
            db.create_all()
            print("Database created successfully!")


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SESSION_PERMANENT"]=False
    app.config["SESSION_TYPE"]='filesystem'
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    from flaskblog.errors.handler import errors
    from flaskblog.main.routes import main
    from flaskblog.posts.routes import posts
    from flaskblog.users.routes import Post, User, users
    from flaskblog.admin.service import PostView, UserView, MyAdminIndexView
    admin = Admin(app, 
                  name="Tai's Blog", 
                  index_view=MyAdminIndexView())
    admin.add_view(UserView(User, db.session))
    admin.add_view(PostView(Post, db.session))
    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(posts)
    app.register_blueprint(errors)
    blueprint = make_github_blueprint(
        client_id=os.environ.get('GITHUB_CLIENT_ID'),
        client_secret=os.environ.get('GITHUB_CLIENT_SECRET'),
    )
    app.register_blueprint(blueprint, url_prefix="/login")

    create_database(app)

    @app.context_processor
    def inject_status():
        return dict(Status=Status)

    return app
