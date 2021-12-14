t = int(input())
for i in range(t):
    d,n = map(int, input().split())
    while d > 1:
        sum = 0
        for j in range(1,n+1):
            sum += j
        d -= 1
        n = sum
    ans = 0
    for x in range(1,n+1):
        ans += x
    print(ans)