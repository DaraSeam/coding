'''
ciel and a-b problem
-> condition
1) output must be the same digit as right ans
2) one of the digit must be wrong but first digit can't be 0
'''
a, b =  map(int, input().split())
s = str(a-b)
if s[0] == '2':
    print(int('3'+s[1:]))
else:
    print(int('2'+s[1:]))