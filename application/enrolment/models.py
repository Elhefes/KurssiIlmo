from application import db

class Enrolment(db.Model):

    __tablename__ = "enrolment"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Date, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    course_id = db.Column(db.Integer, db.ForeignKey('course.id'),
                           nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, course_id, account_id):
        self.course_id = course_id
        self.account_id = account_id
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True