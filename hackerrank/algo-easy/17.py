'''
drawing book
+input: 
-n: number of pages 
-p: page to turn into from the front or the back
+output: 
-minimum value of pages to turn whether from the front or the back
'''
def pageCount(n,p):
    # calculate from the front
    front = p//2
    # calculate from the back
    if n % 2 == 1:
        back = (n-p+1)//2
    else:
        back = (n-p)//2
    return min(front,back)

n = int(input())
p = int(input())
print(pageCount(n,p))