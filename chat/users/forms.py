from .models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError


class SignUpForm(FlaskForm):
		username = StringField('Username:', validators=[DataRequired(), Length(min=2, max=25, message='Username must be min of 2 and max of 25 symbols')])
		email = StringField('Email:', validators=[DataRequired(), Email('Invalid email format')])
		password = PasswordField('Password:', validators=[DataRequired()])
		password2 = PasswordField('Confirm password:', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
		submit = SubmitField('Sign up')


class SignInForm(FlaskForm):
		username = StringField('Username:', validators=[DataRequired(), Length(min=2, max=25, message='Username must be min of 2 and max of 25 symbols')])
		password = PasswordField('Password:', validators=[DataRequired()])
		submit = SubmitField('Sign in')