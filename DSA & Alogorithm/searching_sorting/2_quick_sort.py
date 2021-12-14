def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop() #pivot = list index of sequence
                               #so now we have our pivot
    items_greater = [] #items greater than our pivot
    items_lower = []   #items lower than our pivot
    
    for item in arr:
        if item <= pivot:
            items_lower.append(item)
        else:
            items_greater.append(item)
    
    return quick_sort(items_lower) +[pivot] + quick_sort(items_greater)


print(quick_sort([10,7,8,9,1,5]))
