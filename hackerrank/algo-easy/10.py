# gcd % lcm

# gcd
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

# lcm
def lcm(a,b):
    if a > b:
        higher = a
    else:
        higher = b
        
    value = 1
    while True:
        if higher%a == 0 and higher%b == 0:
            return higher
            break
        else:
            higher *= value
        value += 1

a = int(input())
b = int(input())
print(gcd(a,b))
print(lcm(a,b))