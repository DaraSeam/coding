#the lead game 
#input:
# n: number of rounds
# si, ti: score of player 1&2 each round

#output:
# w: 1or2
# l: max lead score of winner

#condition:
# player with highest lead score of one of the round wins
# 

#(not accepted)
n = int(input())
l_p1 = []
l_p2 = []

for i in range(n):
    p1,p2 = map(int, input().split())
    if p1 > p2:
        p1 -= p2
        l_p1.append(p1)
    else:
        p2 -= p1
        l_p2.append(p2)

if max(l_p1) > max(l_p2):
    print(1,max(l_p1))
else:
    print(2,max(l_p2))

#accpeted (not mine) 
t = int(input())
s1 = 0
s2 = 0
lead = 0
for i in range(t):
    a,b = map(int, input().split())
    s1 = s1 + a 
    s2 = s2 + b
    if(s2-s1 > lead):
        lead = s2-s1
        p = 2 
    elif(s1-s2 > lead):
        lead = s1-s2
        p = 1 

print(p,lead, end=" ")