"""Mono alphabetic/Permutation cipher algorithm"""

import random
import string 

def randomKey():
    # generate alphabet from string
    alphabets = string.ascii_lowercase
    # append to list
    arr = list(alphabets)
    # shuffle items in list
    random.shuffle(arr)
    # join all shuffled items to one string
    randomKey = "".join(arr)
    return randomKey
    
def encryption(plainText, key):
    cipherText = ""
    index = 0
    # convert string to list of alphabet
    listKey = list(key)
    for char in plainText:
        if char.islower():
            index = ord(char) - ord('a')
            cipherText += listKey[index]
        elif char.isupper():
            index = ord(char) - ord('A')
            cipherText += listKey(key)[index]

    return cipherText

# decryption
def decryption(cipherText, key):
    deCipher = ""
    for char in cipherText:
        if char.islower():
            index = key.find(char)
            res = ord('a') + index
            deCipher += chr(res)
    return deCipher
            
# generate randomKey
key = randomKey()
plainText = input("Plain text: ") 

cipherText = encryption(plainText, key)
deCipher = decryption(cipherText, key)
print("Random key: " + key)
print("Cipher text: " + cipherText)
print("DeCipher text: " + deCipher)
