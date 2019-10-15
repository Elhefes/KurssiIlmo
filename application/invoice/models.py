from application import db
from sqlalchemy.sql import text

class Invoice(db.Model):

    __tablename__ = "invoice"
  
    id = db.Column(db.Integer, primary_key=True)
    organizerIban = db.Column(db.String(144),
                           nullable=False)
    enrolment_id = db.Column(db.Integer, db.ForeignKey('enrolment.id'),
                           nullable=False)
    paid = db.Column(db.Boolean, nullable=False)
    price = db.Column(db.Float)

    def __init__(self, course_id, account_id):
        return
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True