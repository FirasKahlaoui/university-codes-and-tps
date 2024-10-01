def cryptageCesar(message, key):
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

def decryptageCesar(message, key):
    return cryptageCesar(message, -key)

text = "Firas is performing an encryption test."
key = 5
encrypted = cryptageCesar(text, key)
decrypted = decryptageCesar(encrypted, key)

print("Texte original:", text)
print("Texte crypté:", encrypted)
print("Texte décrypté:", decrypted)
