'''
sales by match
+input:
-n(int): no. of sock
-arr(arr): array of socks
+output:
-amount of matching socks in arr
'''
from collections import Counter

def sockMerchant(n, arr):
    ans = 0
    count = Counter(arr)
    for i in count:
        ans += count[i]//2
    return ans


n = 7
arr = [10,20,20,10,10,30,50,10,20]
print(sockMerchant(n,arr))