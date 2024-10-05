from flask_mail import Message
from extensions import mail

def send_verification_email(user_email, verification_code):
    try:
        msg = Message('Verification Code', recipients=[user_email])
        msg.body = f'Your verification code is {verification_code}.'
        mail.send(msg)
        print(f'Verification email sent to {user_email} with code {verification_code}')
    except Exception as e:
        print(f'Failed to send verification email: {e}')