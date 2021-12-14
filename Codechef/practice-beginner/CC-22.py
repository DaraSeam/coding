'''
the block game

'''
t = int(input())
for i in range(t):
    n = int(input())
    l = []
    for i in str(n):
        l.append(int(i))
    print("wins") if l[0] == l[-1] else print("loses")