import os
import secrets

from flask import abort, flash, render_template, url_for
from flask.globals import request
from flask_dance.contrib.github import github
from flask_login import current_user, login_required, login_user, logout_user
from PIL import Image
from werkzeug.utils import redirect

from flaskblog import app, bcrypt, db
from flaskblog.forms import (LoginForm, PostForm, RegistrationForm,
                             UpdateAccountForm)
from flaskblog.models import Post, User


# Decorator
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    # Get name picture
    _, f_text = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_text
    picture_path = os.path.join(
        app.root_path, 'static/profile_pics', picture_fn)

    out_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail
    i.save(picture_path)

    return picture_fn

# Infor account
@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post_title = form.title.data
        post_content = form.content.data
        post = Post(title=post_title, content=post_content,
                    author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template("create_post.html", title="Create Post", form=form, name="New Post")


@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title='post', post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Post updated!", 'success')
        return redirect(url_for('post', post_id=post_id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, name="Update Post")


@app.route("/post/<int:post_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted!", 'success')
    return redirect(url_for('home'))
