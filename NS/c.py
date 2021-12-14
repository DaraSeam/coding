# cesar cipher algorithm - encryption and decryption 
"""
step1: get the message to be encrypted 
step2: apply encryption formula base on number of shift we want to encrypt 
step3: encryption process I/P = plainText O/P = cipherText 
        logic: cipherText = ((plainText+numberOfShift) % 26)
step4: decryption process I/P = cipherText O/P = plainText
        logic: plainText = ((cipherText-3) % 26)
"""
import string
plainText = input("Enter the message to be encrypted: ")
shift = int(input("Enter the value to be shifted: "))

# encryption
def encryption(plainText, shift):
    cipherText = ""
    for char in plainText:
    # encrypt char that is lowercase
        if char.islower():
            cipherText += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))

        # encrypt char that is uppercase
        elif char.isupper():
            cipherText += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))

        # encrypt char that is a number
        elif char.isdigit():
            # solution 1
            """
            x = int(char)
            x = (x+shift) % 10
            res = str(x)
            cipherText += res
            """
            # solution 2
            cipherText += chr((ord(char) + shift - ord('0')) % 10 + ord('0'))
        else:
            cipherText += char
    print("This is cipher text: "+cipherText)
    return cipherText

# decryption
def decryption(cipherText):
    shift = 1
    while shift < 10:
        plainText = ""
        for char in cipherText:
            if char.islower():
                plainText += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            elif char.isupper():
                plainText += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            elif char.isdigit():
                x = int(char)
                x = (x-shift) % 10
                res = str(x)
                plainText += res
            else: 
                plainText += char

        print("Key shift "+str(shift) + " output: " + plainText)
        shift += 1


encryption = encryption(plainText, shift)
decryption = decryption(encryption)

