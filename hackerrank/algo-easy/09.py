# kangoroo

def kangoroo(x1,v1,x2,v2):
    count_x1 = x1+v1
    count_x2 = x2+v2
    for i in range(10000):
        if count_x1 == count_x2:
            return "YES"
        count_x1 += v1
        count_x2 += v2
    return "NO"
  
x1,v1,x2,v2 = 0,3,4,2
print(kangoroo(x1,v1,x2,v2))