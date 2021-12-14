#chef and remissness
#input: 
# t = no. of test case
# a,b: counts of how many time chef enter the building from guard A & guard B

#output:
# print min and max of how many time chef enter building respectively

t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    print(max(a,b),a+b)
    
