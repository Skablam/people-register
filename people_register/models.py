from people_register.extensions import db
import json


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    student = db.Column(db.Boolean)
    payment = db.relationship("Payment", back_populates="person")

    def __repr__(self):
        return json.dumps({"id": self.id, "name": self.name, "student": self.student})

    def as_dict(self):
        return {"id": self.id, "name": self.name, "student": self.student}

    @classmethod
    def find(cls, id):
        current_person = cls.query.filter_by(id=id).first()
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
