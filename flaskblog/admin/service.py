
from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):
    form_columns = ["user_name", "email"]
    column_list = ["user_name", "email"]


class PostView(ModelView):
    can_delete = False
    column_list = ["title", "date_posted", "user_id"]
