from people_register.extensions import db
import json


register = db.Table('register',
    db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    student = db.Column(db.Boolean)
    payment = db.relationship("Payment", back_populates="person")
    events = db.relationship("Event", secondary=register, back_populates="people")

    def __repr__(self):
        return json.dumps({"id": self.id, "name": self.name, "student": self.student})

    def as_dict(self):
        return {"id": self.id, "name": self.name, "student": self.student}

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
    people = db.relationship("Person", secondary=register, back_populates="events")

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
