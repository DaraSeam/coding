# birthday
# def birthday(s, d, m):
#     ans=0 #ans = 0, 1, 2,
#     for i in range(len(s)):
#         n=0 
#         count=0
#         while(n<(m)):
#             count+=s[i+n]
#             n+=1
#         # this condition trigger only after while loop is end
#         if(count==d):
#             ans+=1
#         # if count == length of arr it will break and return the result
#         if(i+n==len(s)):
#             break
#     return ans

def birthday(s, d, m):
    ans = 0
    for ele in range(len(s)):
        # declare n to check with m
        # declare count to check with d
        n = 0
        count = 0
        while (n<m):
            count += s[ele+n]
            n += 1
        if count == d:
            ans += 1
        if (ele+n)== len(s):
            break
    return ans


s = [1,2,1,3,2]
d = 3
m = 2
print(birthday(s,d,m))