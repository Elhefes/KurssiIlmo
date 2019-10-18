from application import db
from datetime import datetime, date
from flask_login import login_required, current_user

from sqlalchemy.sql import text

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    location = db.Column(db.String(144), nullable=False)
    startingDate = db.Column(db.Date)
    endingDate = db.Column(db.Date)
    description = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Float)
    organizerIban = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id', ondelete = 'CASCADE'),
                           nullable=False)

    enrolments = db.relationship("Enrolment", backref='course', lazy=True, cascade = "all, delete-orphan")

    def __init__(self, name, location, startingDate, endingDate, description, price, organizerIban):
        self.name = name
        self.location = location
        self.startingDate = startingDate
        self.endingDate = endingDate
        self.description = description
        self.price = price
        self.organizerIban = organizerIban
        self.enroll = False

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

    def get_course_amount():
        stmt = text("SELECT COUNT(*) FROM Course")
        res = db.engine.execute(stmt)
        for row in res:
            return row[0]

    def get_enrollees_amount(self):
        stmt = text("SELECT COUNT(*) FROM Account "
                    "LEFT JOIN Enrolment ON Enrolment.account_id = Account.id "
                    "WHERE Enrolment.course_id = :id").params(id=self.id)
        res = db.engine.execute(stmt)
        for row in res:
            return row[0]

    def has_user_enrolled(self):
        stmt = text("SELECT COUNT(*) FROM Enrolment "
                    "WHERE account_id = :accountId "
                    "AND course_id = :courseId").params(accountId=current_user.id, courseId=self.id)
        res = db.engine.execute(stmt)
        for row in res:
            if (str(row[0]) == "1"):
               return True
        return False
