from flask import render_template, request, redirect, url_for
from datetime import datetime
from flask_login import login_required, current_user

from application import app, db
from application.courses.models import Course
from application.courses.forms import CourseForm

from application.enrolment.models import Enrolment
from application.enrolment.forms import EnrolmentForm

@app.route("/courses/new/")
@login_required
def courses_form():
    return render_template("courses/new.html", form = CourseForm())

@app.route("/courses", methods=["GET"])
def courses_index():
    return render_template("courses/list.html", courses = Course.query.all())

@app.route("/courses/<course_id>/", methods=["POST"])
@login_required
def courses_enroll(course_id):

    t = Course.query.get(course_id)

    if t.enroll == False :
        t.enroll = True
        e = Enrolment(course_id, current_user.id)
        db.session().add(e)
        db.session().commit()
    else:
        enrolmentId = Enrolment.get_enrolment_id(course_id, current_user.id)
        q = Enrolment.query.get(enrolmentId)
        t.enroll = False
        db.session.delete(q)
    
    db.session().commit()
  
    return redirect(url_for("courses_index"))

@app.route("/courses/<course_id>/info", methods=["POST"])

def courses_info(course_id):
    course = Course.query.get(course_id)
    info = Course.query.filter_by(id=course_id).first()

  
    return render_template("courses/info.html", course = course)

@app.route("/courses/<course_id>/edit", methods=["POST"])
@login_required
def courses_edit(course_id):
    t = Course.query.get(course_id)
    db.session.delete(t)
    db.session().commit()

    form = CourseForm(request.form)

    if not form.validate():
        return render_template("courses/edit.html", form = form, course = t)

    t = Course(form.name.data, form.location.data,
    form.startingDate.data, form.endingDate.data, 
    form.description.data, form.price.data)
    
    t.account_id = current_user.id

    db.session().add(t)
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
    form.description.data, form.price.data)
    
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("courses_index"))

@app.route("/courses/<course_id>/delete/", methods=["POST"])
@login_required
def courses_delete(course_id):
    t = Course.query.get(course_id)
    db.session.delete(t)
    db.session().commit()
  
    return redirect(url_for("courses_index"))