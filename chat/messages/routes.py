from .forms import MessageForm
from .models import Message
from chat import app, db, socketio
from flask import render_template, request, escape
from flask_cors import cross_origin
from flask_login import current_user, login_required
import json


@app.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
		title = 'Chat'
		form = MessageForm()
		messages = Message.query.order_by('created')
		return render_template(
			'messages/chat.html', 
			title=title, 
			form=form,
			messages=messages
		)

@socketio.on('message_request')
@cross_origin
def message_request(json, methods=['GET', 'POST']):
		message = Message(
			text=escape(json['text']),
			user_id=current_user.id
		)
		db.session.add(message)
		db.session.commit()
		data = {
			'user': message.author.username,
			'text': message.text,
			'created': message.created.strftime('%H:%M:%S') 
		}
		socketio.emit('message_response', data)