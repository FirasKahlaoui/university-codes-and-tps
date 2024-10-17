import logging
from datetime import datetime
from app.models import Log
from app.extensions import db
from app.db_handler import DBHandler
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Configure the custom DBHandler
db_handler = DBHandler()
db_handler.setLevel(logging.INFO)
logger = logging.getLogger('db_logger')
logger.addHandler(db_handler)

def encrypt_text(plaintext, key, key_size=128):
    key = key.ljust(key_size // 8, '\0')[:key_size // 8]  # Adjust key length
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv + ct

def decrypt_text(encrypted_text, key, key_size=128):
    key = key.ljust(key_size // 8, '\0')[:key_size // 8]  # Adjust key length
    iv = base64.b64decode(encrypted_text[:24])
    ct = base64.b64decode(encrypted_text[24:])
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')

# Log user actions
def log_action(user_id, action):
    log_entry = Log(user_id=user_id, action=action, timestamp=datetime.utcnow())
    db.session.add(log_entry)
    db.session.commit()
    # Log to file and database
    logger.info(action, extra={'user_id': user_id})