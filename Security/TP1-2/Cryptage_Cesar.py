def encrypt_message(message, key):
    encrypted = ""
    for i in range(len(message)):
        character = message[i]
        if character.isalpha():
            if character.isupper():
                encrypted += chr((ord(character) + key - 65) % 26 + 65)
            else:
                encrypted += chr((ord(character) + key - 97) % 26 + 97)
        else:
            encrypted += character
    return encrypted

def decrypt_message(message, key):
    return encrypt_message(message, -key)

