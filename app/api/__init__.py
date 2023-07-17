from flask import Blueprint
from app.api import user_routes

bp = Blueprint('api', __name__)

