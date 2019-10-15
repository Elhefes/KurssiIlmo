from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.input_required(), validators.Length(min = 1, max = 144, message='Käyttäjätunnus täytyy olla pituudeltaan 1-144 merkkiä!')])
    password = PasswordField("Salasana", [validators.input_required(), validators.Length(min = 1, max = 144, message='Salasana täytyy olla pituudeltaan 1-144 merkkiä!')])
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimi", [validators.input_required(), validators.Length(min = 1, max = 144, message='Nimi täytyy olla pituudeltaan 1-144 merkkiä!')])
    username = StringField("Käyttäjätunnus", [validators.input_required(), validators.Length(min = 1, max = 144, message='Käyttäjätunnus täytyy olla pituudeltaan 1-144 merkkiä!')])
    password = PasswordField("Salasana", [validators.input_required(), validators.Length(min = 1, max = 144, message='Salasana täytyy olla pituudeltaan 1-144 merkkiä!')])
  
    class Meta:
        csrf = False