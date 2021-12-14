t = int(input())
for i in range(t):
    list = []
    s = str(input())
    #convert string to list
    for j in s:
        list.append(j)
    #divide list in half
    split = len(list)//2
    if len(list)%2!=0:
        left = list[0:split]
        right = list[split+1:len(list)]
    else:
        left = list[0:split]
        right = list[split:len(list)]
    #sort left and right list
    left.sort()
    right.sort()
    print("YES") if left == right else print("NO")