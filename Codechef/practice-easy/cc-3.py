'''
racing horses
-> condition:
1) find the minimum skill between 2 horses in the stable
'''
# t = int(input())
# for i in range(t):
#     n = int(input())
#     l = list(map(int,input().split()))
#     l.sort() #sort l
#     min = l[1] - l[0] # calculate the least minimum

#     for j in range(0,len(l)-1): #loop through l index
#         new_min = l[j+1] - l[j] #
#         if new_min < min:
#             min = new_min
#     print(min)

t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    min = l[1] - l[0]

    for j in range(0,len(l)-1):
        new_min = l[j+1] - l[j]
        if new_min < min:
            min = new_min
    print(min)