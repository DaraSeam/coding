'''
cats and a mouse
hint: use ABS
'''

def catAndMouse(x,y,z):
    count_x = abs(x-z)
    count_y = abs(y-z)
    if count_x < count_y:
        print("Cat A")
    elif count_y < count_x:
        print("Cat B")
    else:
        print("Mouse C")

x = int(input())
y = int(input())
z = int(input())

print(catAndMouse(x,y,z))