# simple cryptography program to encrypting and decrypting a message
from cryptography.fernet import Fernet

# generate key 
key = Fernet.generate_key()
f = Fernet(key)

# plain text to be encrypted
plainText = bytes(input("Enter a message to be encrypted: "), 'ASCII')

# encryption
def encryption(plainText, f):
    cipherText = f.encrypt(plainText)
    print("Encrypted message is: " + str(cipherText))
    return cipherText

# decryption 
def decryption(plainText, f):  
    result = f.decrypt(encryption(plainText,f))
    return ("Decrypted message is: " + str(result))

print(decryption(plainText,f))