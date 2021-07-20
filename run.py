from chat import socketio, app 


if __name__ == '__main__':
	socketio.run(app, host='192.168.1.6', port=5000, debug=True)