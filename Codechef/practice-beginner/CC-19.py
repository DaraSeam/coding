# ciel and receipt

t = int(input())
for i in range(t):
    p = int(input())
    list = [2048,1024,512,256,128,64,32,16,8,4,2,1]
    sum = 0
    while p > 0:
        for j in list:
            if p >= j:
                div = p//j
                sum += div
                p %= j
    print(sum)

#process