import os
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', '95e1453ba47ad25bcfb83b181a587a55')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///test.db')
db = SQLAlchemy(app)
CORS(app)
socketio = SocketIO(app)
login_manager = LoginManager(app)
login_manager.login_view = 'sign_in'


from chat.users import routes, models
from chat.messages import routes, models