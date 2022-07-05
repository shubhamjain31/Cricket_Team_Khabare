from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField

class TeamForm(FlaskForm):
    name    = TextField('Username',
                         id='name_create',
                         validators=[DataRequired()])
    color   = TextField('Color',
                      id='color_create',
                      validators=[DataRequired()])

    flag    = FileField(id='flag_create')