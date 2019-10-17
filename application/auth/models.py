from application import db
from sqlalchemy.sql import text

class User(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    iban = db.Column(db.String(144), nullable = False)

    courses = db.relationship("Course", backref='account', lazy=True, cascade = "all, delete-orphan")
    enrolments = db.relationship("Enrolment", backref='account', lazy=True, cascade = "all, delete-orphan")

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.iban = ""
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_user_amount():
        stmt = text("SELECT COUNT(*) FROM Account")
        res = db.engine.execute(stmt)
        for row in res:
            return row[0]