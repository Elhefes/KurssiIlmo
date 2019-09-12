from application import app, db
from flask import redirect, render_template, request, url_for
from application.courses.models import Course

@app.route("/courses", methods=["GET"])
def courses_index():
    return render_template("courses/list.html", courses = Course.query.all())

@app.route("/courses/new/")
def courses_form():
    return render_template("courses/new.html")

@app.route("/courses/<course_id>/", methods=["POST"])
def courses_enroll(course_id):

    t = Course.query.get(course_id)
    if t.done == False :
        t.done = True
    else:
        t.done = False
    db.session().commit()
  
    return redirect(url_for("courses_index"))

@app.route("/courses/", methods=["POST"])
def courses_create():
    t = Course(request.form.get("name"), request.form.get("time"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("courses_index"))