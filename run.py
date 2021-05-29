from chat import socketio, app 


if __name__ == '__main__':
	socketio.run(app, cors_allowed_origins="*", debug=True)