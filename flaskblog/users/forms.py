from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import BooleanField, StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import (DataRequired, Email, EqualTo, Length, Optional,
                                ValidationError)

from flaskblog.models import User

current_user: User

class RegistrationForm(FlaskForm):
    user_name = StringField('Username', validators=[
                            DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_user_name(self, user_name):
        user = User.query.filter_by(user_name=user_name.data).first()
        if user:
            raise ValidationError(
                'That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])

    require_password = False

    current_password = PasswordField('Current Password', validators=[Optional()])
    new_password = PasswordField('New Password', validators=[Optional()])
    confirm_password = PasswordField('Confirm New Password', validators=[Optional(), EqualTo('new_password')])

    submit = SubmitField('Update')

    def __init__(self, *args, **kwargs):
        require_password = kwargs.pop('require_password', False)
        super(UpdateAccountForm, self).__init__(*args, **kwargs)

        if require_password:
            self.current_password.validators = [DataRequired()]
            self.new_password.validators = [DataRequired()]
            self.confirm_password.validators = [DataRequired(), EqualTo('new_password')]

    def validate_username(self, username):
        if username.data != current_user.user_name:
            user = User.query.filter_by(user_name=username.data).first()
            if user:
                raise ValidationError(
                    'That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'That email is taken. Please choose a different one.')


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('The user is  not exists!')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
