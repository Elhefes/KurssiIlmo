from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.invoice.models import Invoice
from application.courses.models import Course

from application import app, db

@app.route("/enrolments/<enrolment_id>/<course_id>/invoice", methods=["POST", "GET"])
@login_required
def invoice_index(course_id, enrolment_id):
    course = Course.query.get(course_id)
    return render_template("invoice/invoice.html", course = course, id = enrolment_id)

@app.route("/enrolments/invoice/pay", methods=["POST", "GET"])
@login_required
def invoice_pay(self):
    i = Invoice.query.get(self.id)
    i.paid = True
    db.session().commit()
