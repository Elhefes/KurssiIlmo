from application import db
from sqlalchemy.sql import text

class Enrolment(db.Model):

    __tablename__ = "enrolment"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Date, default=db.func.current_timestamp())
    course_id = db.Column(db.Integer, db.ForeignKey('course.id', ondelete = 'CASCADE'),
                           nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id', ondelete = 'CASCADE'),
                           nullable=False)

    invoices = db.relationship("Invoice", backref='enrolment', lazy=True, cascade = "all, delete-orphan")


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

    def get_enrolment_id(course_id, account_id):
        stmt = text("SELECT id FROM Enrolment WHERE course_id = :courseId AND account_id = :accountId").params(courseId=course_id, accountId=account_id)
        res = db.engine.execute(stmt)
        for row in res:
            return row[0]

    def get_enrolment_amount():
        stmt = text("SELECT COUNT(*) FROM Enrolment")
        res = db.engine.execute(stmt)
        for row in res:
            return row[0]

    def get_enrollee_name(self):
        stmt = text("SELECT name FROM Account WHERE id = :userId").params(userId = self.account_id)
        res = db.engine.execute(stmt)
        for row in res:
            return row[0]

    def enrolment_getCourse(self):
        stmt = text("SELECT name FROM Course WHERE id =:course_id ").params(course_id=self.course_id)
        res = db.engine.execute(stmt)
        for row in res:
            return row[0]
    
    def is_invoice_paid(self):
        stmt = text("SELECT paid FROM Invoice WHERE enrolment_id =:enrolmentId ").params(enrolmentId=self.id)
        res = db.engine.execute(stmt)
        for row in res:
            return row[0]

    def get_enrollees(course_id):
        stmt = text("SELECT * FROM Account "
                "LEFT JOIN Enrolment ON Enrolment.account_id = Account.id "
                "WHERE Enrolment.course_id = :id ").params(id=course_id)
        res = db.engine.execute(stmt)
        result = []
        for row in res:
            result.append(row)

        return result