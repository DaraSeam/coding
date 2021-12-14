''' 
migratory birds
input: array of sighted bird of each type(index) Ex: index(0)=type(0), index(1)=type(1)...
output: return index with most value, if value is equal return the lowest index of the two Ex: type(1):4, type(4):4 => return type(1)
'''

def migratoryBirds( arr):
    count = [0 for i in range(6)] # create arr with 0 value: count = [0,0,0,0,0,0]
    for birds in arr:
        count[birds] = count[birds] + 1
    return count.index(max(count)) # return lowest type with most sighted. Ex: type4:3

arr = [1,4,4,4,5,3]
print(migratoryBirds(arr))