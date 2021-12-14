'''
condition:
1) tax is 8%
2) n: price/can without tax
3) with tax: (1.08 * n)
4) if tax-included < 206yen, return Yay!
5) if tax-included == 206yen, return so-so
6) if tax-included > 206yen, return :(
'''

n = int(input())
withTax = n*1.08
priceList = 206
if int(withTax) < priceList:
    print("Yay!")
elif int(withTax) == priceList:
    print("so-so")
else:
    print(":(")