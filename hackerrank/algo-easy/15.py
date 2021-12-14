'''
bonAppetit
input:
bill(array of int): bill that have to split between 2 Brian and Anna
k(int): index of the item that Anna did not eat
b(int): amount of money Brian charge Anna after split
output: 
if, Brian overcharged Anna, return b_charge - b_actual
if, Brian did not overcharged Anna, return "Bon Appetit"
'''

def bonAppetit(bill,k,b):
    total = 0
    bill.remove(bill[k])
    for item in bill:
        total += item

    if (total//2) == b:
        return "Bon Appetit"
    else:
        return int(b-(total/2))
 
k = int(input())
bill = list(map(int,input().rstrip().split()))
b = int(input())
print(bonAppetit(bill,k,b))