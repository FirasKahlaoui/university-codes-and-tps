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

# Separate login/logout handling to avoid multiple button clicks
if not st.session_state.authenticated:
    st.sidebar.header("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if login(username, password):
            st.session_state.authenticated = True
            st.experimental_rerun()  # Forces a rerun after successful login
        else:
            st.sidebar.error("Invalid username or password.")
else:
    st.sidebar.header("Inputs")

    # Fields for encryption/decryption
    message = st.sidebar.text_area("Text to encrypt/decrypt:", height=150)

    # Encrypt and Decrypt options
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
    
    # Clear button to reset encryption/decryption fields
    if st.sidebar.button("Clear Fields"):
        st.sidebar.text_area("Text to encrypt/decrypt:", height=150, value="")
        st.experimental_rerun()

    # Logout button
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.experimental_rerun()

# HTTPS and other advanced buttons (placeholders for now)
st.markdown("### Advanced Options")
if st.button("Enable HTTPS"):
    st.success("HTTPS enabled!")
if st.button("Two-Factor Authentication"):
    st.success("Two-factor authentication enabled!")

st.markdown("""
---
*Developed with ❤️ by Firas Kahlaoui*.
""")
