from flask import request, Blueprint, Response, request, render_template, redirect
from flask import current_app
from people_register.models import Event, Person
from people_register.extensions import db
import json
import time

# This is the blueprint object that gets registered into the app in blueprints.py.
events = Blueprint('events', __name__)

@events.route("")
def add_event():
    if request.method == "GET":
        events = Event.query.filter_by()

        return render_template("events.html", events=events)
    elif request.method == "POST":
        new_event = Event()
        new_event.name = request.form.get("name")

        db.session.add(new_event)
        db.session.commit()

        return Response(status=201)

@events.route("/today")
def get_todays_event():

    current_date = time.strftime("%Y-%m-%d")

    current_event = Event.find_by_date(current_date)

    if current_event is not None:
        return Response(response=repr(current_event), mimetype="application/json", status=200)
    else:
        new_event = Event()
        new_event.date = current_date
        new_event.name = "Weekly Classes"

        db.session.add(new_event)
        db.session.commit()

        return Response(response=repr(current_event), mimetype="application/json", status=200)


@events.route("/<event_id>/register", methods=["GET", "POST"])
def get_event_register(event_id):

    current_event = Event.find(event_id)

    current_person = Person.find_by_name(request.args.get("fullname"))

    # If the person hasn't been added before then add them
    if current_person is None:
        current_person = Person()
        current_person.name = register_req["name"]

    current_event.people.append(current_person)

    db.session.add(current_event)
    db.session.commit()

    return redirect("/home")
