
from flask import (Blueprint, flash, redirect, render_template, request,
                   session, url_for)
from flask_dance.contrib.github import github
from flask_login import current_user, login_required, login_user, logout_user

from flaskblog import bcrypt, db
from flaskblog.models import Post, Status, User, has_access
from flaskblog.users.forms import (LoginForm, RegistrationForm,
                                   RequestResetForm, ResetPasswordForm,
                                   UpdateAccountForm)
from flaskblog.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)
current_user: User

@users.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(user_name=form.user_name.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been create!', 'success')
        return redirect(url_for('users.login'))

    return render_template('register.html', title='Register', form=form)

# User login
@users.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user: User = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            # check the admin approve your account are not
            is_approve: User=User.query.filter_by(id=user.id).first()
            if has_access(is_approve.status, {Status.INACTIVE, 
                                              Status.BANNED, 
                                              Status.PENDING}):
            # if is_approve.status == Status.USER:
                flash('Your Account is not approved by Admin','danger')
            else:
                login_user(user, remember=form.remember.data)
                # next page is account
                next_page = request.args.get('next')
                session['user_id']=user.id
                session['user_name']=user.user_name
                flash('Login Successfully','success')
                return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsucessful. Please check email and password', 'danger')
    return render_template('login.html', title="Login", form=form)

# User logout
@users.route("/logout")
def logout():
    if not session.get('user_id'):
        return redirect(url_for('main.home'))

    logout_user()
    session['user_id'] = None
    session['user_name'] = None
    return redirect(url_for('main.home'))


# Infor account
@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    require_password = request.form.get('change_password') == 'on'
    form = UpdateAccountForm(require_password=require_password)

    if form.validate_on_submit():
        current_user.user_name = form.username.data
        current_user.email = form.email.data

        # Update picture
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        # If password is required, check if current password is correct
        if require_password:
            if not current_user.check_password(form.current_password.data):
                flash('Incorrect current password', 'danger')
                return redirect(url_for('users.account'))

            current_user.set_password(form.new_password.data)

        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        form.username.data = current_user.user_name
        form.email.data = current_user.email
    image_file = url_for(
        'static', filename='profile_pics/' + current_user.image_file)

    return render_template('account.html', title='Account', image_file=image_file, form=form)

@users.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type = int)
    user = User.query.filter_by(user_name = username).first_or_404()
    posts = Post.query.filter_by(author = user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page = page, per_page = 5)
    return render_template('user_posts.html', posts = posts, user = user)

@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email reset password has been sent to your email!', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@users.route("/reset_token/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user: User = User.verify_reset_token(token)
    if user is None:
        flash('That is invalid token!', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been updated!', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Token', form=form)

@users.route("/gitlogin")
def gitlogin():
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok
    print(resp.json())
    return "You are @{login} on GitHub".format(login=resp.json()["login"])
