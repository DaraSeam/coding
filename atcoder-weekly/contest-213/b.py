n = int(input())
a = list(map(int,input().split()))
sorted_a = []
for i in a:
    sorted_a.append(i)
sorted_a.sort(reverse = True)
temp = sorted_a[1]
for j in range(len(a)):
    if a[j] == temp:
        print(j+1)