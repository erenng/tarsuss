from flask import request
from app.api import bp
from app.controller import user_controller


@bp.route('/createNewUser', methods=['POST'])
def create_user():
    return user_controller.create_new_user_controller(request)

@bp.route('/login', methods=['POST'])
def login():
    return user_controller.login_controller(request)

