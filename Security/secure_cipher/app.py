import os
from flask import Flask, render_template, redirect, url_for, flash, request, session
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from email_service import send_verification_email
from two_factor import generate_verification_code
from forms import RegistrationForm, LoginForm
from extensions import db, mail

# Load environment variables from .env file
load_dotenv()  # Load the environment variables from the .env file

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.example.com')  # Change to your SMTP server
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True') == 'True'  # Convert to boolean
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Fetch email from environment variables
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Fetch password from environment variables

db.init_app(app)
mail.init_app(app)

# Create your database model here (User model)
from database import create_db, User

with app.app_context():
    create_db()  # Ensure the database is created within the application context

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            hashed_password = generate_password_hash(form.password.data, method='sha256')
            new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Your account has been created!', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()  # Rollback the session in case of error
            flash(f'An error occurred: {e}', 'danger')
            print(f'Error: {e}')  # Print the error to the terminal for debugging
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('two_factor'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/two_factor', methods=['GET', 'POST'])
def two_factor():
    if request.method == 'POST':
        input_code = request.form.get('verification_code')
        actual_code = session.get('verification_code')
        if input_code == actual_code:
            user = User.query.get(session['user_id'])
            user.is_verified = True
            db.session.commit()
            return redirect(url_for('home'))
        else:
            flash('Invalid verification code', 'danger')
    return render_template('two_factor.html')

@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    if not user.is_verified:
        return redirect(url_for('two_factor'))
    
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)