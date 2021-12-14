n = int(input())
givenName = []
lastName = []
for i in range(n):
    s,t = list(map(str,input().split()))
    givenName.append(s)
    lastName.append(t)

firstGivenName = givenName[0]
firstLastName = lastName[0]
firstNameCount = 0
lastNameCount = 0
for i in range(1, len(givenName)):
    if givenName[i] == firstGivenName:
        firstNameCount += 1

for i in range(1, len(lastName)):
    if lastName[i] == firstLastName:
        lastNameCount += 1
if firstNameCount == 1 and lastNameCount == 1:
    print("Yes")
else:
    print("No")