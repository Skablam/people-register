from people_register.extensions import db
import json


class Entry(db.Model):
    __tablename__ = 'entry'
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    level = db.Column(db.String)
    person = db.relationship("Person", back_populates="events")
    event = db.relationship("Event", back_populates="entries")

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    student = db.Column(db.Boolean)
    member = db.Column(db.Boolean)
    member_timestamp = db.Column(db.DateTime)
    payment = db.relationship("Payment", back_populates="person")
    events = db.relationship("Entry", back_populates="person")

    def __repr__(self):
        return json.dumps({"id": self.id, "name": self.name, "student": self.student})

    def as_dict(self):
        return {"id": self.id, "name": self.name, "member": self.member}

    @classmethod
    def find(cls, id):
        current_person = cls.query.filter_by(id=id).first()
        return current_person

    @classmethod
    def find_by_name(cls, name):
        current_person = cls.query.filter_by(name=name).first()
        return current_person


class Payment(db.Model):
    __tablename__ = 'payment'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    date = db.Column(db.Date)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    person = db.relationship("Person", back_populates="payment")

    def __repr__(self):
        return json.dumps({"id": self.id, "amount": self.amount, "date": self.date, "person": self.person_id})

class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    name = db.Column(db.String)
    entries = db.relationship("Entry", back_populates="event")

    def __repr__(self):
        return json.dumps({"id": self.id, "name": self.name, "date": self.date.strftime("%Y-%m-%d")})

    @classmethod
    def find(cls, id):
        current_event = cls.query.filter_by(id=id).first()
        return current_event

    @classmethod
    def find_by_date(cls, date):
        current_event = cls.query.filter_by(date=date).first()
        return current_event

    @classmethod
    def find_by_date_and_name(cls, date, name):
        current_event = cls.query.filter_by(name=name, date=date).first()
        if current_event is not None:
            return False, current_event
        else:
            current_event = cls.create_event(date, name)
            db.session.add(current_event)
            db.session.commit()
            return True, current_event

    @classmethod
    def create_event(cls, date, name):
        new_event = Event()
        new_event.date = date
        new_event.name = name
        return new_event
