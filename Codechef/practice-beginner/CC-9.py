#lucky four
#input:
# t: no of test case

#output:
# no of ouccurance of 4 of each test case

t =int(input())
for i in range(t):
    ans = 0
    n = int(input())
    for i in str(n):
        if i == '4':
            ans += 1
    print(ans)