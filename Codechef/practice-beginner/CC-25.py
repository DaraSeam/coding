'''
id and ship
input: 
'''

t = int(input())
for i in range(t):
    b = ['b', 'B']
    c = ['c', 'C']
    d = ['d', 'D']
    f = ['f', 'F']
    char = input()
    if char in b:
        print("BattleShip")
    elif char in c:
        print("Cruiser")
    elif char in d:
        print("Destroyer")
    elif char in f:
        print("Frigate")
    else:
        print()