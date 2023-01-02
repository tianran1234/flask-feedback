"""Forms for flask-feedback."""

from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm

class RegisterForm(FlaskForm):
    """User registration form."""

    username=StringField('Username', validators=[InputRequired(), Length(min=3, max=20)] )
    password=PasswordField('Password', validators=[InputRequired(), Length(min=3, max=20)])
    Email=StringField('Email', validators=[InputRequired(), Email(), Length(max=20)])
    first_name=StringField('First Name', validators=[InputRequired(), Length(max=20)] )
    last_name=StringField('Last Name', validators=[InputRequired(), Length(max=20)])


class LoginForm(FlaskForm):
    """User login form."""

    username=StringField('Username', validators=[InputRequired()])
    password=PasswordField('Password', validators=[InputRequired()])


class FeedbackForm(FlaskForm):
    """Add/Modify feedback form."""

    title = StringField('Title', validators=[InputRequired(), Length(max=100)])
    content = StringField('Content', validators=[InputRequired()])
