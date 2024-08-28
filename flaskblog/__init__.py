
import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_dance.contrib.github import github, make_github_blueprint
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

app = Flask(__name__)

db = SQLAlchemy()
bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category ='info'
mail = Mail()

app.secret_key = "b2dd17eb994d430edbc07467c6805875"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com' # Địa chỉ máy chủ SMTP sử dụng để gửi email
app.config['MAIL_PORT'] = 587 # Cổng máy chủ SMTP (thường là 587 với TLS hoặc 465 với SSL).
app.config['MAIL_USE_TLS'] = True # Bật hoặc tắt sử dụng TLS (Transport Layer Security) cho kết nối email.
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
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
