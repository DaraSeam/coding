'''
problem: smallest no. of notes
given: note = [2,5,10,50,100]
input:
t: no. of test case
n: int following t

output:
return smalles t no. of notes that combine to give n
'''

t = int(input())
for i in range(t):
    n = int(input())
    notes = [100,50,10,5,2,1]
    ans = 0
    while n > 0:
        for j in notes:
            if j <= n:
                div = n//j
                ans += div
                n %= j
    print(ans)