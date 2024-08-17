from flask import render_template

from flaskblog import app
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


@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template('login.html', title="Login")
