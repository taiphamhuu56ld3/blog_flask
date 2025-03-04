from flask import render_template
from flaskblog import app

from flaskblog.models import Post


# Decorator
@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")
