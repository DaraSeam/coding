#sums in a triangle
#wrong 
t = int(input())
for x in range(t):
    n = int(input())
    ans = []
    for i in range(n):
        sum=0
        l = list(map(int,input().split()))
        for j in l:
            sum+=j
        ans.append(sum)
    ans.sort()
    print(ans[-1])