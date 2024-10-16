from flask import render_template, redirect, url_for, flash, Blueprint, session, request
from flask_login import login_user, current_user, login_required, logout_user
from app.extensions import db, bcrypt
from app.forms import LoginForm, AdminCreateUserForm, OTPForm
from app.models import User, Admin, Log
from app.utils import log_action, generate_otp, send_otp
from app.decorators import nocache

main = Blueprint('main', __name__)


@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            otp = generate_otp()
            session['otp'] = otp
            send_otp(user.email, otp)
            return redirect(url_for('main.verify_otp'))
        flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', form=form)


@main.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if 'otp' not in session:
        return redirect(url_for('main.login'))
    form = OTPForm()
    if form.validate_on_submit():
        if form.otp.data == session['otp']:
            session.pop('otp', None)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid OTP. Please try again.', 'danger')
    return render_template('verify_otp.html', form=form)


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
        existing_user = User.query.filter_by(email=form.email.data).first(
        ) or Admin.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already exists. Please use a different email.', 'danger')
        elif form.password.data != form.confirm_password.data:
            flash('Passwords do not match. Please try again.', 'danger')
        else:
            try:
                hashed_password = bcrypt.generate_password_hash(
                    form.password.data).decode('utf-8')
                if form.is_admin.data:
                    user = Admin(username=form.username.data,
                                 email=form.email.data, password=hashed_password)
                else:
                    user = User(username=form.username.data,
                                email=form.email.data, password=hashed_password)
                db.session.add(user)
                db.session.commit()
                log_action(current_user.id, f'Created user {user.username}')
                flash('User created successfully!', 'success')
            except Exception as e:
                db.session.rollback()
                flash(
                    'An error occurred while creating the user. Please try again.', 'danger')
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
