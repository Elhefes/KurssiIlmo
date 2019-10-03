from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.courses.models import Course

from application import app, db

@app.route("/enrolments", methods=["GET"])
def enrolments_index():
    return render_template("enrolment/list.html", courses = Course.query.all())