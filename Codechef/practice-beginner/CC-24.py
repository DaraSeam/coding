#primality test
t = int(input())
for i in range(t):
    n = int(input())
    if n > 1:
        for j in range(2,n):
            if n%j==0:
                print('no')
                break
        else:
            print('yes')
    else:
        print("no")
