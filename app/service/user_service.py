from app.db import user_db
from app.models.user_models import User


def get_user_by_email_service(email):
    return user_db.get_user_by_email(email)


def create_user_service(data):
    user = User()
    user.from_dict(data)
    return user_db.insert_user(user)


