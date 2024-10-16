import os
import pyotp
from flask_mail import Message
import logging
from datetime import datetime
from app.models import Log
from app.extensions import db, mail
from app.db_handler import DBHandler
from msal import ConfidentialClientApplication

# Configure the custom DBHandler
db_handler = DBHandler()
db_handler.setLevel(logging.INFO)
logger = logging.getLogger('db_logger')
logger.addHandler(db_handler)


def encrypt_text(plaintext, shift):
    encrypted = ""
    for char in plaintext:
        # Shift character using Unicode values
        shifted = ord(char) + shift
        encrypted += chr(shifted)
    return encrypted


def decrypt_text(encrypted_text, shift):
    decrypted = ""
    for char in encrypted_text:
        shifted = ord(char) - shift
        decrypted += chr(shifted)
    return decrypted

# Log user actions


def log_action(user_id, action):
    log_entry = Log(user_id=user_id, action=action,
                    timestamp=datetime.utcnow())
    db.session.add(log_entry)
    db.session.commit()

    # Log to file and database
    logger.info(action, extra={'user_id': user_id})


def generate_otp():
    totp = pyotp.TOTP(pyotp.random_base32())
    return totp.now()


def get_oauth2_token():
    client_id = os.environ.get('CLIENT_ID')
    client_secret = os.environ.get('CLIENT_SECRET')
    tenant_id = os.environ.get('TENANT_ID')
    authority = f"https://login.microsoftonline.com/{tenant_id}"
    app = ConfidentialClientApplication(
        client_id, authority=authority, client_credential=client_secret)
    result = app.acquire_token_for_client(
        scopes=["https://outlook.office365.com/.default"])
    return result['access_token']


def send_otp(email, otp):
    token = get_oauth2_token()
    msg = Message('Your OTP Code', sender=os.environ.get('MAIL_DEFAULT_SENDER'),
                  recipients=[email])
    msg.body = f'Your OTP code is {otp}. It will expire in 5 minutes.'
    mail.send(msg, auth=('user', token))
