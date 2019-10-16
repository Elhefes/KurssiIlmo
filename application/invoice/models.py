from application import db
from sqlalchemy.sql import text

class Invoice(db.Model):

    __tablename__ = "invoice"
  
    id = db.Column(db.Integer, primary_key=True)
    enrolment_id = db.Column(db.Integer, db.ForeignKey('enrolment.id'),
                           nullable=False)
    price = db.Column(db.Float)
    paid = db.Column(db.Boolean, nullable=False)

    def __init__(self, enrolment_id, price):
        self.enrolment_id = enrolment_id
        self.price = price
        self.paid = False

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True