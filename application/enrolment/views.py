from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.enrolment.models import Enrolment
from application.courses.views import Course

from application import app, db

@app.route("/enrolments", methods=["GET"])
@login_required
def enrolments_index():
    return render_template("enrolment/list.html", enrolments = Enrolment.query.all())

@app.route("/enrolments/<course_id>/remove", methods=["POST"])
@login_required
def enrolments_remove(course_id):
    enrolmentId = Enrolment.get_enrolment_id(course_id, current_user.id)
    q = Enrolment.query.get(enrolmentId)
    db.session.delete(q)
    db.session().commit()
  
    return redirect(url_for("enrolments_index"))