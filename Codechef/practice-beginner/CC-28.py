'''
gross salary
input:
t: no. of test case
salary: basic salary

output: 
return gross salary 
'''

#brute force
t = int(input())
for i in range(t):
    salary = int(input())
    if salary < 1500:
        hra = 10*salary/100
        da = 90*salary/100
        gs = salary+hra+da
        print("{:.2f}".format(gs))
    elif salary >= 1500:
        hra = 500
        da = 98*salary/100
        gs = salary+hra+da
        print("{:.2f}".format(gs))