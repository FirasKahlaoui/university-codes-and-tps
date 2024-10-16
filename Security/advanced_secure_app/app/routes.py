from flask import Blueprint, render_template, request, redirect, url_for, flash, session, send_file
from flask_login import current_user, login_user, login_required
from app import db, bcrypt
from app.models import User
from app.forms import LoginForm
from app.utils import generate_totp_secret, get_totp_uri, generate_qr_code
import pyotp

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)


@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('auth.verify_2fa'))
        flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', form=form)


@auth.route('/setup_2fa')
@login_required
def setup_2fa():
    if current_user.totp_secret is None:
        secret = generate_totp_secret()
        current_user.totp_secret = secret
        db.session.commit()
    else:
        secret = current_user.totp_secret

    uri = get_totp_uri(current_user.email, secret)
    qr_code = generate_qr_code(uri)
    return send_file(qr_code, mimetype='image/png')


@auth.route('/verify_2fa', methods=['GET', 'POST'])
@login_required
def verify_2fa():
    if request.method == 'POST':
        token = request.form.get('token')
        totp = pyotp.TOTP(current_user.totp_secret)
        if totp.verify(token):
            flash('2FA setup successful', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid token, please try again', 'danger')
    return render_template('verify_2fa.html')


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
