from flask import abort, redirect, request, url_for
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from flaskblog.utils import Status


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.status == Status.ADMIN

    def inaccessible_callback(self, name, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('users.login', next=request.url))

        if current_user.status != Status.ADMIN:
            abort(403)
        # redirect to login page if user doesn't have access
        return redirect(url_for('users.login', next=request.url))

    @expose('/')
    def index(self):
        if not current_user.is_authenticated and current_user.status == Status.ADMIN:
            return redirect(url_for('users.login'))
        return super(MyAdminIndexView, self).index()


class UserView(ModelView):
    form_columns = ["user_name", "email", "image_file", "status"]
    column_list = ["user_name", "email", "status"]


class PostView(ModelView):
    can_delete = False
    column_list = ["title", "date_posted", "author"]

    column_labels = {
        "author": "Author"
    }

    def _author_formatter(view, context, model, name):
        return model.author.user_name

    column_formatters = {
        "author": _author_formatter
    }
