#Enormous input test

#input
#n
#k

#output
#how many integers of n are divisible by k

n,k = map(int, input().split())
res = 0
for i in range(n):
    i = int(input())
    if i%k == 0:
        res += 1
print(res)