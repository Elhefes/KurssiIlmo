from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.enrolment.models import Enrolment
from application.courses.models import Course
from application.invoice.models import Invoice

from application import app, db

@app.route("/enrolments", methods=["GET"])
@login_required
def enrolments_index():
    return render_template("enrolment/list.html", enrolments = Enrolment.query.all(), invoice = Invoice.query.all())

@app.route("/enrolments/<course_id>/remove", methods=["POST"])
@login_required
def enrolments_remove(course_id):
    enrolmentId = Enrolment.get_enrolment_id(course_id, current_user.id)
    invoice = Invoice.query.filter_by(enrolment_id = enrolmentId).first()
    db.session.delete(invoice)
    db.session().commit()

    e = Enrolment.query.get(enrolmentId)
    db.session.delete(e)
    db.session().commit()
  
    return redirect(url_for("enrolments_index"))