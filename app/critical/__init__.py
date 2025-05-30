from flask import Blueprint

bp = Blueprint('critical', __name__)

from app.critical import routes