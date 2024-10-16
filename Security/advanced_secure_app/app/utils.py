import os
import pyotp
import qrcode
from io import BytesIO
from flask import send_file
import logging
from datetime import datetime
from app.models import Log
from app.extensions import db
from app.db_handler import DBHandler

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


def generate_totp_secret():
    return pyotp.random_base32()


def get_totp_uri(user_email, secret):
    return pyotp.totp.TOTP(secret).provisioning_uri(user_email, issuer_name="YourAppName")


def generate_qr_code(uri):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(uri)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer


def generate_otp():
    totp = pyotp.TOTP(pyotp.random_base32())
    return totp.now()
