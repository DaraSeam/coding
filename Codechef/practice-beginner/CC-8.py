#turbo sort
#input:
# t: num of nums in list
# n: nums that need to be sorted

#output: given num in non decreasing order
n = []
t = int(input())
for i in range(t):
    n.append(int(input()))
n.sort()
for j in n:
    print(j)