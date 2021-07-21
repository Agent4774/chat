from .forms import SignUpForm, SignInForm
from .models import User
from chat import app, db
from flask import render_template, url_for, redirect, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def home():
		if current_user.is_authenticated:
			return redirect(url_for('chat'))
		return redirect(url_for('sign_in'))

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
		if current_user.is_authenticated:
				return redirect(url_for('chat'))
		title = 'Chat | Sign up'
		form = SignUpForm()
		if form.validate_on_submit():
				user = User(
					username=form.username.data,
					email=form.email.data,
					password=generate_password_hash(form.password.data)
				)
				db.session.add(user)
				db.session.commit()
				flash('Congrats! You have been signed up! Please, log in', 'success')
				return redirect(url_for('sign_in'))
		return render_template('users/sign_up.html', title=title, form=form)

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
		if current_user.is_authenticated:
				return redirect(url_for('chat'))
		title = 'Chat | Sign in'
		form = SignInForm()
		if form.validate_on_submit():
				user = User.query.filter_by(username=form.username.data).first()
				if not user:
						flash('Invalid username or password', 'danger')
						return redirect(url_for('sign_in'))
				if not check_password_hash(user.password, form.password.data):
						flash('Invalid username or password', 'danger')
						return redirect(url_for('sign_in'))
				login_user(user)
				return redirect(url_for('chat'))
		return render_template('users/sign_in.html', title=title, form=form)

@app.route('/log-out', methods=['GET'])
def log_out():
		logout_user()
		return redirect(url_for('sign_in'))