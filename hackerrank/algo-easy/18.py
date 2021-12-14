'''
electronic shop
+input:
-b: budget
-keyboard: array of keyboard models
-drives: array of drives models
+condition:
+output:
-maximum that can spent on both devices
+solution: compare the max of sum between previous money spent with new one
'''

def getMoneySpent(keyboards,drives,b):
    moneySpent = -1
    for i in keyboards:
        for j in drives:
            if (i+j) <= b:
                moneySpent = max(moneySpent, i+j)
    return moneySpent

keyboards = [3,1]
drives = [5,2,8]
b = 10
print(getMoneySpent(keyboards, drives, b))