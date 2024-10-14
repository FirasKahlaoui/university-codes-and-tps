from flask import render_template, redirect, url_for, flash, Blueprint, session
from flask_login import login_user, current_user, login_required, logout_user
from app.extensions import db, bcrypt
from app.forms import LoginForm, AdminCreateUserForm
from app.models import User, Admin, Log
from app.utils import log_action
from app.decorators import nocache

main = Blueprint('main', __name__)


@main.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            log_action(user.id, 'Logged in')
            return redirect(url_for('main.dashboard'))
        flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', form=form)


@main.route("/admin_login", methods=['GET', 'POST'])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=form.email.data).first()
        if admin and bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin)
            log_action(admin.id, 'Logged in')
            return redirect(url_for('main.admin_dashboard'))
        flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('admin_login.html', form=form)


@main.route("/dashboard")
@login_required
@nocache
def dashboard():
    return render_template('dashboard.html')


@main.route("/admin_dashboard", methods=['GET', 'POST'])
@login_required
@nocache
def admin_dashboard():
    form = AdminCreateUserForm()
    if form.validate_on_submit():
        # Check if email already exists
        existing_user = User.query.filter_by(email=form.email.data).first() or Admin.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already exists. Please use a different email.', 'danger')
        elif form.password.data != form.confirm_password.data:
            flash('Passwords do not match. Please try again.', 'danger')
        else:
            try:
                hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                if form.is_admin.data:
                    user = Admin(username=form.username.data, email=form.email.data, password=hashed_password)
                else:
                    user = User(username=form.username.data, email=form.email.data, password=hashed_password)
                db.session.add(user)
                db.session.commit()
                log_action(current_user.id, f'Created user {user.username}')
                flash('User created successfully!', 'success')
            except Exception as e:
                db.session.rollback()
                flash('An error occurred while creating the user. Please try again.', 'danger')
                print(f"Error: {e}")
            return redirect(url_for('main.admin_dashboard'))
    users = User.query.all()
    admins = Admin.query.all()
    logs = Log.query.all()
    return render_template('admin_dashboard.html', form=form, users=users, admins=admins, logs=logs)


@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))
