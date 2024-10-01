import streamlit as st
from Cryptage_Cesar import cryptageCesar, decryptageCesar

st.title("🔐 Caesar Cipher")

st.markdown("""
## Welcome to the Caesar Cipher Application
Use this application to encrypt and decrypt messages using the Caesar cipher.
""")

st.sidebar.header("Inputs")
message = st.sidebar.text_area("Text to encrypt/decrypt:", height=150)
key = st.sidebar.number_input(
    "Encryption key:", min_value=0, max_value=25, step=1)

if st.sidebar.button("Encrypt"):
    encrypted_message = cryptageCesar(message, key)
    st.markdown(f"### Encrypted Text:\n**<span style='font-size:20px; color:#FF1493;'>{encrypted_message}</span>**", unsafe_allow_html=True)

if st.sidebar.button("Decrypt"):
    decrypted_message = decryptageCesar(message, key)
    st.markdown(f"### Decrypted Text:\n**<span style='font-size:20px; color:#FF1493;'>{decrypted_message}</span>**", unsafe_allow_html=True)

st.markdown("""
---
*Developed with ❤️ by Firas Kahlaoui*.
""")