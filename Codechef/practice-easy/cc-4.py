'''
uncle johny
input:
n:
a:
k:

output: 
return the position of k after sorted

condition:
1) remember k position before sorted
2) print k position after sorted
'''
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    k = int(input())
    k-=1
    old_idx = a[k]
    a.sort()
    ans = a.index(old_idx) + 1
    print(ans)