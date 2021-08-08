from flask_wtf import FlaskForm
from wtforms import TextAreaField


class MessageForm(FlaskForm):
	message = TextAreaField()