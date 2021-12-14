# quick sort

def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    else: 
        pivot = arr.pop()

    #lower and higher arr
    left_arr = []
    right_arr = []

    for i in range(0,len(arr)):
        if arr[i] <= pivot:
            left_arr.append(arr[i])
        else:
            right_arr.append(arr[i])
            
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)


arr_test = [10,7,8,9,1,5]
print(quick_sort(arr_test))
