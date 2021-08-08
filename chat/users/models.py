from chat import app, db, login_manager
from flask_login import UserMixin
from chat.messages.models import Message


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)
	

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(255), nullable=False)
	is_admin = db.Column(db.Boolean, nullable=False, default=False)
	is_staff = db.Column(db.Boolean, nullable=False, default=False)
	messages = db.relationship(Message, backref='author', lazy=True)

	def __repr__(self):
		return f'User({self.username})'