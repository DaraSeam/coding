# sum of digits
#input:
# t: total number of test case 
# n: each line contain n

#output:
#calculate the sum digits of n and display in new line

t = int(input())
for i in range(t):
    n = int(input())
    ans = 0
    for j in str(n):
        ans += int(j)
    print(ans)