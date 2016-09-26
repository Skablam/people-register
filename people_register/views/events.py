from flask import request, Blueprint, Response, request, render_template, redirect
from flask import current_app
from people_register.models import Event, Person, Entry
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
        newly_created, new_event = Event.find_by_date_and_name(time.strftime("%Y-%m-%d"), request.form.get("name"))

        current_app.logger.info("New event created - {0}".format(repr(new_event)))

        return Response(status=201)

@events.route("/today")
def get_todays_weekly_event():

    newly_created, current_event = Event.find_by_date_and_name(time.strftime("%Y-%m-%d"), "Weekly Classes")

    return Response(response=repr(current_event), mimetype="application/json", status=200)

@events.route("/<event_id>/register", methods=["GET", "POST"])
def get_event_register(event_id):

    current_event = Event.find(event_id)
    new_entry = Entry(level=request.args.get("level"))
    current_person = Person.find_by_name(request.args.get("fullname"))

    # If the person hasn't been added before then add them
    if current_person is None:
        current_person = Person()
        current_person.name = request.args.get("fullname")

    if request.args.get("member") == "true":
        current_person.member = True
        current_person.member_timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    else:
        current_person.member = False

    new_entry.person = current_person
    current_event.entries.append(new_entry)

    db.session.add(current_event)
    db.session.commit()

    return redirect("/home")
