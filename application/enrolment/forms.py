from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class EnrolmentForm(FlaskForm):
    username = StringField("Käyttäjätunnus")

  
    class Meta:
        csrf = False