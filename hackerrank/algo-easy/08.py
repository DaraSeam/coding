# countApplesAndOranges

def countApplesAndOranges(s,t,a,b,apples,oranges):
    res_a = 0
    res_b = 0
    for i in range(len(apples)):
        if (a+apples[i]) in range(s,t+1):
            res_a += 1
    
    for j in range(len(oranges)):
        if (b+oranges[j]) in range(s,t+1):
            res_b += 1
    
    print(res_a)
    print(res_b)


s = 7
t = 11
a = 5
b = 15
apples = list(map(int,input().split()))
oranges = list(map(int,input().split()))
countApplesAndOranges(s,t,a,b,apples,oranges)