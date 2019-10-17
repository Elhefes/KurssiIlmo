from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.invoice.models import Invoice
from application.courses.models import Course

from application import app, db

@app.route("/enrolments/<enrolment_id>/<course_id>/invoice", methods=["POST", "GET"])
@login_required
def invoice_index(course_id, enrolment_id):
    course = Course.query.get(course_id)
    invoice = Invoice.query.filter_by(enrolment_id = enrolment_id).first()
    print (invoice.paid)
    return render_template("invoice/invoice.html", course = course, id = enrolment_id, invoice = invoice)

@app.route("/enrolments/<invoice_id>/pay", methods=["POST", "GET"])
@login_required
def invoice_pay(invoice_id):
    i = Invoice.query.get(invoice_id)
    i.paid = True
    db.session().commit()
    return redirect(url_for("enrolments_index"))