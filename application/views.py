from flask import render_template
from application import app
from application.courses.models import Course
from application.auth.models import User

@app.route("/")
def index():
    return render_template("index.html", user = User, course = Course)