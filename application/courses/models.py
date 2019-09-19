from application import db
from datetime import datetime, date

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    location = db.Column(db.String(144), nullable=False)
    startingDate = db.Column(db.DateTime)
    endingDate = db.Column(db.DateTime)
    description = db.Column(db.String(144), nullable=False)
    enroll = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, location, startingDate, endingDate, description):
        self.name = name
        self.location = location
        self.startingDate = startingDate
        self.endingDate = endingDate
        self.description = description
        self.enroll = False
