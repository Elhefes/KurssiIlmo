from application import db
from datetime import datetime, date

from sqlalchemy.sql import text

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    location = db.Column(db.String(144), nullable=False)
    startingDate = db.Column(db.Date)
    endingDate = db.Column(db.Date)
    description = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Float)

    enroll = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, location, startingDate, endingDate, description, price):
        self.name = name
        self.location = location
        self.startingDate = startingDate
        self.endingDate = endingDate
        self.description = description
        self.price = price
        self.enroll = False

    def get_organiser_name(self):
        
        stmt = text("SELECT Account.name FROM Account JOIN Course ON Account.id"
                    "= Course.account_id WHERE Course.id = :id").params(id=self.id)
        res = db.engine.execute(stmt)
        for row in res:
            return row[0]