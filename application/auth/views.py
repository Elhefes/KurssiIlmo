from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import User
from application.courses.models import Course
from application.enrolment.models import Enrolment
from application.invoice.models import Invoice
from application.auth.forms import LoginForm, RegisterForm, EditForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Väärä käyttäjätunnus tai salasana")

    login_user(user)
    return redirect(url_for("courses_index"))

@app.route("/auth/register", methods=["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form = RegisterForm())

    form = RegisterForm(request.form)
    if not form.validate():
        return render_template("auth/registerform.html", form = form)
    
    user = User.query.filter_by(username=form.username.data).first()
    if user:
        return render_template("auth/registerform.html", form = form, 
                                error = "Käyttäjänimi on jo käytössä!")
    
    t = User(form.name.data, form.username.data, form.password.data)

    db.session().add(t)
    db.session().commit()

    login_user(t)
    return redirect(url_for("courses_index"))

@app.route("/courses/edit", methods=["GET", "POST"])
@login_required
def auth_edit():
    return render_template("auth/editform.html", form = EditForm())

@app.route("/auth/modify", methods = ["GET", "POST"])
def auth_modify():
    form = EditForm(request.form)
    if not form.validate():
        return render_template("auth/editform.html", form = form)
    
    u = User.query.get(current_user.id)
    u.name = form.name.data
    u.username = form.username.data
    u.password = form.password.data
    u.iban = form.iban.data

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("courses_index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/delete/", methods=["POST"])
@login_required
def account_delete():

    e = Enrolment.query.filter_by(account_id = current_user.id)
    for enrolment in e:
        ownInvoice = Invoice.query.filter_by(enrolment_id = enrolment.id).first()
        db.session().delete(ownInvoice)
        db.session().delete(enrolment)

    c = Course.query.filter_by(account_id = current_user.id)
    for course in c:
        e = Enrolment.query.filter_by(course_id = course.id)
        for enrolment in e:
            ownInvoice = Invoice.query.filter_by(enrolment_id = enrolment.id).first()
            db.session.delete(ownInvoice)
            db.session().delete(enrolment)
        db.session().delete(course)

    u = User.query.get(current_user.id)
    db.session.delete(u)
    db.session().commit()
    return redirect(url_for("index"))