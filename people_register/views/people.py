from flask import request, Blueprint, Response, request
from flask import current_app
from people_register.models import Person
from people_register.extensions import db
import json

# This is the blueprint object that gets registered into the app in blueprints.py.
people = Blueprint('people', __name__)


@people.route("", methods=["POST"])
def add_person():

    new_person = Person()
    new_person.name = request.form.get("name")

    db.session.add(new_person)
    db.session.commit()

    return Response(status=201)

@people.route("/search")
def search_for_person():

    search_name = request.args.get("name")

    people = Person.query.filter(Person.name.like("%{0}%".format(search_name))).all()

    people_list = []
    for person in people:
        people_list.append(person.as_dict())

    search_response = json.dumps({"people" : people_list})

    return Response(response=search_response, mimetype="application/json", status=200)

@people.route('/<person_reference>', methods=['GET', 'PUT', 'DELETE'])
def get_people(person_reference):
    if request.method == 'GET':
        # Use case: Retrieve a gadget with an id of person_reference and return
        # it to the user
        current_app.logger.info("Retrieve person {0} from the database".format(person_reference))
        current_person = Person.find(id=person_reference)

        if current_person is not None:
            return Response(response=repr(current_person), status=200)
        else:
            return Response(status=404)
    elif request.method == 'PUT':
        # Use case: Update the gadget in the database with an id of person_reference.
        person_request = request.json

        current_person = Person.find(id=person_reference)

        if current_person is not None:
            current_person.name = person_request["name"]
            current_person.student = person_request["student"]

            db.session.add(current_person)
            db.session.commit()

            return Response(response=repr(current_person), status=200)
        else:
            return Response(status=404)
    elif request.method == 'DELETE':
        # Use case: Delete the gadget from the database with an id of person_reference
        current_person = Person.find(id=person_reference)

        if current_person is not None:
            db.session.delete(current_person)
            db.session.commit()

            return Response(status=200)
        else:
            return Response(status=404)
