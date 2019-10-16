from flask import render_template, request, redirect, url_for
from datetime import datetime
from flask_login import login_required, current_user

from application import app, db
from application.courses.models import Course
from application.courses.forms import CourseForm

from application.enrolment.models import Enrolment
from application.invoice.models import Invoice

@app.route("/courses/new/")
@login_required
def courses_form():
    return render_template("courses/new.html", form = CourseForm())

@app.route("/courses/<course_id>/edit", methods=["POST"])
@login_required
def courses_edit_form(course_id):
    c = Course.query.get(course_id)
    return render_template("courses/edit.html", form = CourseForm(), course = c, courseStart = 
        (str(c.startingDate.year)+"-"+str(c.startingDate.month)+"-"+str(c.startingDate.day)), courseEnd =
        (str(c.endingDate.year)+"-"+str(c.endingDate.month)+"-"+str(c.endingDate.day)))

@app.route("/courses", methods=["GET"])
def courses_index():
    return render_template("courses/list.html", courses = Course.query.all(), enrolments = Enrolment.query.all())

@app.route("/courses/<course_id>/info", methods=["POST"])
def courses_info(course_id):
    course = Course.query.get(course_id)  
    return render_template("courses/info.html", course = course)

@app.route("/courses/<course_id>/modify", methods=["POST"])
@login_required
def courses_modify(course_id):
    c = Course.query.get(course_id)
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("courses/edit.html", form = form, course = c, courseStart = 
        (str(c.startingDate.year)+"-"+str(c.startingDate.month)+"-"+str(c.startingDate.day)), courseEnd =
        (str(c.endingDate.year)+"-"+str(c.endingDate.month)+"-"+str(c.endingDate.day)))

    c.name = form.name.data
    c.location = form.location.data
    c.startingDate = form.startingDate.data
    c.endingDate = form.endingDate.data
    c.description = form.description.data
    c.price = form.price.data

    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("courses_index"))

@app.route("/courses/", methods=["POST"])
@login_required
def courses_create():
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("courses/new.html", form = form)

    t = Course(form.name.data, form.location.data,
    form.startingDate.data, form.endingDate.data, 
    form.description.data, form.price.data, form.organizerIban.data)

    if current_user.iban == "":
        current_user.iban = form.organizerIban.data

    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("courses_index"))

@app.route("/courses/<course_id>/delete/", methods=["POST"])
@login_required
def courses_delete(course_id):
    e = Enrolment.query.filter_by(course_id = course_id)
    for i in e:
        db.session().delete(i)

    t = Course.query.get(course_id)
    db.session.delete(t)
    db.session().commit()
  
    return redirect(url_for("courses_index"))

@app.route("/courses/<course_id>/", methods=["POST"])
@login_required
def enroll(course_id):
    e = Enrolment(course_id, current_user.id)
    db.session().add(e)

    c = Course.query.get(course_id)
    if c.price > 0:
        i = Invoice(e.id, c.price)
        db.session().add(i)

    db.session().commit()
    
    return redirect(url_for("courses_index"))

@app.route("/courses/<course_id>/remove", methods=["POST"])
@login_required
def remove_enrolment(course_id):
    enrolmentId = Enrolment.get_enrolment_id(course_id, current_user.id)
    q = Enrolment.query.get(enrolmentId)
    db.session.delete(q)
    db.session().commit()
  
    return redirect(url_for("courses_index"))