from datetime import datetime
from app.models import Log
from app import db

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
    log_entry = Log(user_id=user_id, action=action, timestamp=datetime.utcnow())
    db.session.add(log_entry)
    db.session.commit()
