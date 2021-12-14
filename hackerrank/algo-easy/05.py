# min-max

def miniMaxSum(arr):
    arr.sort()
    max = arr[1:]
    min = arr[:-1]
    print(sum(min),sum(max))
arr = [1,2,3,4,5]
print(miniMaxSum(arr))