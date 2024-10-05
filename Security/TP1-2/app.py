import streamlit as st
from database import create_table, register_user, check_user
from two_factor import send_verification_code
from Cryptage_Cesar import encrypt_message, decrypt_message

# Ensure the database table is created
create_table()

# Streamlit app title
st.title("🔐 Secure Cipher with 2FA")

# Add a sidebar for navigation
st.sidebar.header("Navigation")
if st.sidebar.checkbox("Register"):
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Register"):
        if register_user(username, password):
            st.sidebar.success("User registered successfully!")
        else:
            st.sidebar.error("Username already exists.")

if st.sidebar.checkbox("Login"):
    username = st.sidebar.text_input("Username (Login)")
    password = st.sidebar.text_input("Password (Login)", type="password")
    if st.sidebar.button("Login"):
        if check_user(username, password):
            email = st.sidebar.text_input("Email for 2FA")
            verification_code = send_verification_code(email)
            user_code = st.sidebar.text_input("Enter verification code sent to your email:")
            if user_code == str(verification_code):
                st.sidebar.success("Logged in successfully!")

                # Encryption/Decryption Interface
                message = st.text_area("Message")
                key = st.number_input("Caesar Cipher Key", min_value=1, max_value=25)

                # Buttons for encryption and decryption
                if st.button("Encrypt"):
                    if message:
                        encrypted_message = encrypt_message(message, key)
                        st.success(f"Encrypted Message: {encrypted_message}")
                    else:
                        st.error("Please enter a message to encrypt.")

                if st.button("Decrypt"):
                    if message:
                        decrypted_message = decrypt_message(message, key)
                        st.success(f"Decrypted Message: {decrypted_message}")
                    else:
                        st.error("Please enter a message to decrypt.")

                # Clear fields button
                if st.button("Clear Fields"):
                    st.session_state.message = ""
                    st.session_state.key = 0
                    st.success("Fields cleared!")

                # Logout button
                if st.button("Logout"):
                    st.sidebar.success("Logged out successfully.")
                    # Optionally, you can redirect to the login/register page here

# Footer
st.markdown("""
---
*Developed with ❤️ by Firas Kahlaoui*.
""")
