from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, HiddenField
  
class EnrolmentForm(FlaskForm):
    course_id = HiddenField("hiddenField")
  
    class Meta:
        csrf = False