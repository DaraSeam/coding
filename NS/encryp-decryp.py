from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

# secret messages
plain_text = bytes(input("Enter the message to be encrypted: "), 'ASCII')

# encrypt
cipher_text = f.encrypt(plain_text)
print("Encrypted message is: " +str(cipher_text))

# decrypt
decrypt = f.decrypt(cipher_text)
print("Decrypted message is: " +str(decrypt))
