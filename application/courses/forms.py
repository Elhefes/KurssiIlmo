from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, DateField, TextAreaField
from datetime import datetime

class CourseForm(FlaskForm):
    name = StringField("Kurssin nimi", [validators.Length(min=2, max=15)])
    location = StringField("Paikka", [validators.Length(min=2, max=15)])
    startingDate = DateField('Alku', [validators.InputRequired(message='Kurssin aika')], default=datetime.now())
    endingDate = DateField('Loppu', [validators.InputRequired(message='Kurssin aika')], default=datetime.now())
    description = TextAreaField('Kuvaus', [validators.Length(min=2, max=300)])
    price = StringField('Hinta', default = "0")
    enroll = BooleanField("Done")

    class Meta:
        csrf = False