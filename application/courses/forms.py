from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, DateField, TextAreaField, ValidationError
from datetime import datetime

class CourseForm(FlaskForm):
    name = StringField("Kurssin nimi", [validators.Length(min=1, max=50, message='Kurssin nimen täytyy olla pituudeltaan 1-50 merkkiä!')])
    location = StringField("Paikka", [validators.Length(min=1, max=50, message='Paikan nimen täytyy olla pituudeltaan 1-50 merkkiä!')])
    startingDate = DateField('Alku', [validators.InputRequired(message='Kurssin aika')], default=datetime.now())
    endingDate = DateField('Loppu', [validators.InputRequired(message='Kurssin aika')], default=datetime.now())
    description = TextAreaField('Kuvaus', [validators.Length(min=1, max=1000, message='Kuvauksen täytyy olla pituudeltaan 1-1000 merkkiä!')])
    price = StringField('Hinta', default = "0.0")
    organizerIban = StringField('Pankkitilin numero')
    
    def validate_startingDate(form, field):
        if field.data > form.endingDate.data:
            raise ValidationError('Kurssin loppupäivämäärä ei voi olla ennen alkamispäivämäärää')

    def validate_price(form, field):
        try:
            float(field.data)
        except ValueError:
            raise ValidationError('Hinta täytyy olla numeerinen luku. Erota pisteellä eurot ja sentit.')

    def validate_organizerIban(form, field):
        if float(form.price.data) > 0:
            if form.organizerIban.data == "":
                raise ValidationError('Jos kurssi on maksullinen, laitathan laskulle tilinumeron!')

    class Meta:
        csrf = False