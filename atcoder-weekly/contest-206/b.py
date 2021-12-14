n = int(input())
ans = 0
yen = 0
for i in range(1,n+1):
    yen += i
    if yen < n:
        ans += 1
print(ans)