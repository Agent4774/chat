from chat import app, db
from datetime import datetime


class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.Text)
	created = db.Column(db.DateTime, default=datetime.now)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return f'Message({self.created.strftime("%Y-%m-%d %H:%M:%S")})'