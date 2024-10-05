from flask_mail import Message
from extensions import mail

def send_verification_email(user_email, verification_code):
    msg = Message('Verification Code', sender='noreply@example.com', recipients=[user_email])
    msg.body = f'Your verification code is {verification_code}.'
    mail.send(msg)