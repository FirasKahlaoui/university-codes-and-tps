import streamlit as st
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_message(message):
    return cipher_suite.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message):
    return cipher_suite.decrypt(encrypted_message.encode()).decode()

# User authentication
def login(username, password):
    # Simple hardcoded credentials for demonstration
    return username == "FirasKahlaoui" and password == "Firascrypt"

# Streamlit app
st.title("🔐 Secure Cipher")

st.markdown("""
## Welcome to the Secure Cipher Application
Use this application to encrypt and decrypt messages using a secure cipher.
""")

# Login form
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.sidebar.header("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if login(username, password):
            st.session_state.authenticated = True
            st.sidebar.success("Login successful!")
        else:
            st.sidebar.error("Invalid username or password.")
else:
    st.sidebar.header("Inputs")
    message = st.sidebar.text_area("Text to encrypt/decrypt:", height=150)
    key = st.sidebar.number_input("Encryption key:", min_value=0, max_value=25, step=1)

    if st.sidebar.button("Encrypt"):
        if message:
            encrypted_message = encrypt_message(message)
            st.markdown(f"### Encrypted Text:\n**<span style='font-size:20px; color:#FF1493;'>{encrypted_message}</span>**", unsafe_allow_html=True)
        else:
            st.sidebar.error("Message cannot be empty.")

    if st.sidebar.button("Decrypt"):
        if message:
            decrypted_message = decrypt_message(message)
            st.markdown(f"### Decrypted Text:\n**<span style='font-size:20px; color:#FF1493;'>{decrypted_message}</span>**", unsafe_allow_html=True)
        else:
            st.sidebar.error("Message cannot be empty.")

    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.sidebar.success("Logged out successfully.")

st.markdown("""
---
*Developed with ❤️ by Firas Kahlaoui*.
""")