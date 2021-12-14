#grade the steel
t = int(input())
for i in range(t):
    h,cc,ts = map(float,input().split())
    cond_1 = h > 50
    cond_2 = cc < 0.7
    cond_3 = ts > 5600
    if cond_1 and cond_2 and cond_3:
        print(10)
    elif cond_1 and cond_1:
        print(9)
    elif cond_2 and cond_3:
        print(8)
    elif cond_1 and cond_3:
        print(7)
    elif cond_1 or cond_2 or cond_3:
        print(6)
    else:
        print(5)