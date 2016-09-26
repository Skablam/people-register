from flask import request, Blueprint, Response, render_template
from flask import current_app
from people_register.models import Person, Event
import json
import time

# This is the blueprint object that gets registered into the app in blueprints.py.
register = Blueprint('register', __name__)


@register.route("/")
@register.route("/home")
def home():
    headers = {"cache-control": "no-store"}

    newly_created, current_event = Event.find_by_date_and_name(time.strftime("%Y-%m-%d"), "Weekly Classes")

    return render_template("home.html", entries=current_event.entries, headers=headers)
