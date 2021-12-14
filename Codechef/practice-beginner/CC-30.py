t = int(input())
for i in range(t):
    t1 = int(input())
    n = list(map(int, input().split()))
    n.sort()
    print(n[0]+n[1])