from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, DateField, TextAreaField, ValidationError
from datetime import datetime

class CourseForm(FlaskForm):
    name = StringField("Kurssin nimi", [validators.Length(min=2, max=15, message='Kurssin nimen täytyy olla pituudeltaan 2-15 merkkiä!')])
    location = StringField("Paikka", [validators.Length(min=2, max=15, message='Paikan nimen täytyy olla pituudeltaan 2-15 merkkiä!')])
    startingDate = DateField('Alku', [validators.InputRequired(message='Kurssin aika')], default=datetime.now())
    endingDate = DateField('Loppu', [validators.InputRequired(message='Kurssin aika')], default=datetime.now())
    description = TextAreaField('Kuvaus', [validators.Length(min=2, max=300, message='Kuvauksen täytyy olla pituudeltaan 2-300 merkkiä!')])
    price = StringField('Hinta', default = "0")
    
    def validate_startingDate(form, field):
        if field.data > form.endingDate.data:
            raise ValidationError('Kurssin loppupäivämäärä ei voi olla ennen alkamispäivämäärää')

    def validate_price(form, field):
        try:
            float(field.data)
        except ValueError:
            raise ValidationError('Hinta täytyy olla numeerinen luku. Erota pisteellä eurot ja sentit.')

    class Meta:
        csrf = False