#packaging cupcakes
#input:
# t: no. of test case
# n: no. of cupcakes
#output:
# print no. of leftover cupcakes

t = int(input())
for i in range(t):
    n = int(input())
    print(n-t) if (n>t) else print(n)