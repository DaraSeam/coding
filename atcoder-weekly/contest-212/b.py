x = int(input())
l = []
for i in str(x):
    l.append(int(i))
if l.count(l[0]) == 4:
    print("Weak")

for j in range(len(l)-1):
    next_index = l[j+1]
    prev_index = l[j]
    if next_index - prev_index == 1 or next_index - prev_index == -9:
        print("Weak")
        break
    else:
        print("Strong")
        break
    

        
    
