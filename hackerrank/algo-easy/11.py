# breaking records

def breakingRecords(scores):
    max, min = scores[0], scores[0]
    max_count, min_count = 0,0
    for i in range(1, len(scores)):
        temp = scores[i]
        if temp > max:
            max = temp
            max_count += 1
        else:
            if temp < min:
                min = temp 
                min_count += 1
    return max_count, min_count

# scores = [10,5,20,20,4,5,2,25,1]
scores = list(map(int,input().strip().split()))
print(breakingRecords(scores))