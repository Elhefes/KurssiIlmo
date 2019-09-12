from application import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    time = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.done = False
