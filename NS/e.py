"""
play fair cipher - matrix - key matrix
create a key matrix
"""
import string

'''
get keyword and create keyMatrix 5x5
'''
keyWord = input("Enter keyword: ")
alphabets = string.ascii_lowercase
alphabets = alphabets.replace('j', '.')
keyMatrix = ['' for i in range(5)] # create 5 empty string


row, column = 0,0
print()
print("Alphabet after replace: ")
for char in keyWord: 
    if char in alphabets: 
        keyMatrix[row] += char
        alphabets = alphabets.replace(char, '.')
        
        print(alphabets)
        column += 1

        if column > 4: 
            row += 1
            column = 0

print()
print("Key matrix with keyword only: ")
print(keyMatrix)

for char in alphabets: 
    if (char != '.'):
        keyMatrix[row] += char
        column += 1
        if column > 4:
            row += 1
            column = 0
print()
print("The final key matrix: ")
print(keyMatrix)