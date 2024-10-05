import os
from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from email_service import send_verification_email
from two_factor import generate_verification_code
from forms import RegistrationForm, LoginForm

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

db = SQLAlchemy(app)
mail = Mail(app)

# Create your database model here (User model)
from database import create_db, User
create_db()  # Ensure the database is created

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = generate_password_hash(form.password.data)

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        verification_code = generate_verification_code()
        send_verification_email(email, verification_code)
        session['verification_code'] = verification_code
        session['user_email'] = email
        
        flash('Registration successful! Please check your email for verification.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            if user.is_verified:
                verification_code = generate_verification_code()
                send_verification_email(user.email, verification_code)
                session['verification_code'] = verification_code
                session['user_id'] = user.id
                
                flash('Login successful! Please check your email for the verification code.', 'success')
                return redirect(url_for('two_factor'))
            else:
                flash('Please verify your email first.', 'warning')
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/two_factor', methods=['GET', 'POST'])
def two_factor():
    if request.method == 'POST':
        user_code = request.form.get('verification_code')
        if user_code == str(session.get('verification_code')):
            user = User.query.get(session['user_id'])
            flash('Login successful! Welcome!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid verification code. Please try again.', 'danger')
    
    return render_template('two_factor.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
