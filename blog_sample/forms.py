from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email

class AuthorForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    website = StringField('Website', validators=[DataRequired()])
    photo = StringField('Foto', validators=[DataRequired()])
    bio = TextAreaField('Bio', validators=[DataRequired()])
