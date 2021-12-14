#second largest
#input:
# a,b,c: integer to compare which is second largest

t = int(input())
l = []
for i in range(t):
    l = []
    a,b,c = map(int, input().split())
    l.append(a)
    l.append(b)
    l.append(c)
    l.sort()
    print(l[1])