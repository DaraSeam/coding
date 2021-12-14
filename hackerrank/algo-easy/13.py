# divisible sum pairs
def divisibleSumPairs(n,k,ar):
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i] + ar[j]) % k == 0:
                ans += 1
    return ans

n = 6
k = 3
ar = [1,3,2,6,1,2]
print(divisibleSumPairs(n,k,ar))