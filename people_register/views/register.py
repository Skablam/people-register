from flask import request, Blueprint, Response, render_template
from flask import current_app
import json

# This is the blueprint object that gets registered into the app in blueprints.py.
register = Blueprint('register', __name__)


@register.route("/home")
def home():
    return render_template("home.html")