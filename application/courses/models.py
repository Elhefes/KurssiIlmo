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

    def edit(self, name, location, startingDate, endingDate, description, price):
        return 0

    def get_organiser_name(self):
        stmt = text("SELECT Account.name FROM Account JOIN Course ON Account.id"
                    "= Course.account_id WHERE Course.id = :id").params(id=self.id)
        res = db.engine.execute(stmt)
        for row in res:
            return row[0]

    def get_organiser_id(self):
        stmt = text("SELECT Account.id FROM Account JOIN Course ON Account.id"
                    "= Course.account_id WHERE Course.id = :id").params(id=self.id)
        res = db.engine.execute(stmt)
        for row in res:
            return row[0]

    def get_course_amount(self):
        stmt = text("SELECT COUNT(*) FROM Course")
        res = db.engine.execute(stmt)
        for row in res:
            return row[0]

    def get_enrollees(self):
        stmt = text("SELECT Account.name FROM Account "
                    "LEFT JOIN Enrolment ON Enrolment.account_id = Account.id "
                    "WHERE Enrolment.course_id = :id "
                    "GROUP BY Account.name").params(id=self.id)
        res = db.engine.execute(stmt)
        
        return res