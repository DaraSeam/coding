#merge_sort

def merge_sort(arr):
    if len(arr) > 1:
        #split arr in half

        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        #merge
        l = 0 #left_arr index
        r = 0 #right_arr index
        m = 0 #merge_arr index

        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] < right_arr[r]:
                arr[m] = left_arr[l] #left_arr and merge_arr doesn't change        
                                      #because we swap arr[0] = 5 with left_arr[0] = 5         
                l += 1 #increment to loop to next index of left_arr
            else:
                arr[m] = right_arr[r]
                r += 1
            m += 1 #increment to loop to next index of merge_arr
        
        while l < len(left_arr):    # check again if l < left_arr or not 
            arr[m] = left_arr[l]    # if still < left_arr keep swapping arr between left_arr
            l += 1
            m += 1
        
        while r < len(right_arr):   # check again if l < right_arr or not 
            arr[m] = right_arr[r]   # if still < right_arr keep swapping arr between right_arr
            r += 1
            m += 1

        


arr_test = [5,7,8,9,1,10,2]
merge_sort(arr_test)
print(arr_test)