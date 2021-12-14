# staircase
# bruteforce

def staircase(n):
    # temp = "#"
    # i = 0
    # while i < n:
    #     print(temp.rjust(n))
    #     temp += "#"
    #     i += 1
    # quit()


# shorter solution
    for i in range(1,n+1):
        print((i*"#").rjust(n))
        
n = int(input())
print(staircase(n))