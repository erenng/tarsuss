from app.db import user_db
from app.models.user_models import User, hash_password


def get_user_by_email_service(email):
    return user_db.get_user_by_email(email)


def create_user_service(data):
    user = User()
    user.from_dict(data)
    user.password = hash_password(user.password)
    return user_db.insert_user(user)


def auth_user_service(password, email):
    user = user_db.get_user_by_email(email)
    print(1)
    if user:
        if user.check_password(password):
            print("1")
            return True
    return False
