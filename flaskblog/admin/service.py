
from flask_admin.contrib.sqla import ModelView


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
