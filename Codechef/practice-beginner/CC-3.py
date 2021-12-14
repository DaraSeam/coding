#add two numbers
#t: number of test cases
#a,b: number that need to be add

t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    print(a+b)