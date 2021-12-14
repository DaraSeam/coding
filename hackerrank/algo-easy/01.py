# compareTriplets

def compareTriplets(a, b):
    alice,bob = 0,0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        if a[i] < b[i]:
            bob += 1
    return [alice,bob]
a = list(map(int,input().rstrip().split()))
b = list(map(int,input().rstrip().split()))
print(compareTriplets(a,b))