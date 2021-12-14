n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
res = []
for i in a:
    for j in b:
        ans = i-j
        res.append(abs(ans))
print(min(res))
