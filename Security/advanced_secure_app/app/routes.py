# Security/advanced_secure_app/app/routes.py
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
        login_type = form.login_type.data
        if login_type == 'user':
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                log_action(user.id, 'Logged in')
                return redirect(url_for('main.dashboard'))
        elif login_type == 'admin':
            admin = Admin.query.filter_by(email=form.email.data).first()
            if admin and bcrypt.check_password_hash(admin.password, form.password.data):
                login_user(admin)
                log_action(admin.id, 'Logged in')
                return redirect(url_for('main.admin_dashboard'))
        flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', form=form)


@main.route("/dashboard")
@login_required
@nocache
def dashboard():
    return render_template('dashboard.html')


@main.route("/admin_dashboard", methods=['GET', 'POST'])
@login_required
@nocache
def admin_dashboard():
    admin = Admin.query.filter_by(id=current_user.id).first()
    if not admin:
        flash('You are not authorized to access the admin dashboard.', 'danger')
        return redirect(url_for('main.dashboard'))

    form = AdminCreateUserForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,
                    password=hashed_password, is_verified=form.is_admin.data)
        db.session.add(user)
        db.session.commit()
        log_action(current_user.id, f'Created user {user.username}')
        flash(f'User {user.username} has been created!', 'success')

    users = User.query.all()
    logs = Log.query.all()
    return render_template('admin_dashboard.html', users=users, logs=logs, form=form)


@main.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect(url_for('main.login'))
