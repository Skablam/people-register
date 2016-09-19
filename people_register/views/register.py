from flask import request, Blueprint, Response, render_template
from flask import current_app
from people_register.models import Person
import json

# This is the blueprint object that gets registered into the app in blueprints.py.
register = Blueprint('register', __name__)


@register.route("/")
@register.route("/home")
def home():
    people = Person.query.filter_by()

    return render_template("home.html", people=people)

@register.route("/register/people")
def get_all_people():
    people = Person.query.filter_by()

    return render_template("people.html", people=people)
