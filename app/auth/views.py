from flask import render_template, request, redirect, url_for, abort, flash
from . import auth
from werkzeug.urls import url_parse
from .forms import RegistrationForm, LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from ..models import *
from app import db, bcrypt
# from ..email import mail_message

@auth.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)





@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))
