t = int(input())
for i in range(t):
    q,p = map(int, input().split())
    if q > 1000:
        #using formula whole = p*100/%
        whole = q*p
        #part = whole*%/100
        part = (10*24000)/100
        print(whole-part)
    else:
        print(q*p)
