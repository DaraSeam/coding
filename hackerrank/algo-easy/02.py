# diagonol diffrences
# brute-force code 
# def diagonalDifference(arr):
#         len_arr = len(arr)
#         i,j = 0,0
#         left_diagonal = 0
#         while i < len_arr:
#             left_diagonal += arr[i][j]
#             i += 1
#             j += 1
        
#         i = 0
#         j = len_arr - 1
#         right_diagonal = 0
#         while i < len_arr:
#             right_diagonal += arr[i][j]
#             i += 1
#             j -= 1
#         return abs(left_diagonal - right_diagonal)


# organized code from sapanz
def diagonalDifference(arr):
    left,right = 0,0
    length = len(arr[0])

    for count in range(length):
        left += arr[count][count]
        right += arr[count][length-count-1]
    
    return abs(left-right)

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().rstrip().split())))
print(diagonalDifference(arr))