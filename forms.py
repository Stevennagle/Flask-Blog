from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

#Need to ensure user-entered text is not a script or command
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
