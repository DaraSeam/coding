#first and last digit
#input:
#t: total no of test case
#n: integer follow by t

t = int(input())
for i in range(t):
    n = str(input())
    print(int(n[0])+int(n[-1]))