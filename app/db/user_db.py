from app import db
from app.models.user_models import User


def get_user_by_email(email):
    return db.session.query(User).filter(User.email == email).first()


def insert_user(user):
    try:
        db.session.add(user)
        db.session.commit()
        return True
    except:
        return False