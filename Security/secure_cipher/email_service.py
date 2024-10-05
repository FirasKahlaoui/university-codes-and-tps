from flask_mail import Mail, Message
from flask import current_app

mail = Mail()

def send_verification_email(user_email, verification_code):
    msg = Message('Email Verification', sender='your_email@example.com', recipients=[user_email])
    msg.body = f'Your verification code is: {verification_code}'
    mail.send(msg)
