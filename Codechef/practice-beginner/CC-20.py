#mahasena

n = int(input())
l = []
odd_l = []
for i in range(n):
    a = int(input())
    l.append(a)
    even_l = []
    for j in l:
        if j%2==0:
            even_l.append(j)
for x in l:
    if x % 2 != 0:
        odd_l.append(x)
print("READY FOR BATTLE") if len(even_l) > len(odd_l) else print("NOT READY")

#OPTIMAL NOT MINE
N = int(input())

A = list(map(int, input().split()))
lCount = 0
unCount = 0

for num in A:
    if num % 2 == 0:
        lCount += 1
    else:
        unCount += 1
        
if lCount > unCount:
    print('READY FOR BATTLE')
else:
    print('NOT READY')