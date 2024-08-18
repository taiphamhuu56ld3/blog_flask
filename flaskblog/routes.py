from flask import flash, render_template, url_for
from flask.globals import request
from flask_login import login_user
from werkzeug.utils import redirect

from flaskblog import app, bcrypt
from flaskblog.forms import LoginForm
from flaskblog.models import User

posts = [
    {
        'author': 'Tai',
        'title': 'Page',
        'content': "This is Content",
        'date_posted': 'August 15, 2024'
    }
]

# Decorator
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods = ["POST", "GET"])
def register():
    return render_template('register.html', title = 'Register')

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # next page is account
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsucessful. Please check email and password', 'danger')
    return render_template('login.html', title="Login", form=form)
