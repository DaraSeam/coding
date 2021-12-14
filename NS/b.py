# simple python programming
s = list(input().strip())
hash_c, star_c = s.count("#"), s.count("*")

if hash_c == star_c: 
    print("Valid string")
else:
    if hash_c > star_c:
        count = 0
        while star_c < hash_c:
            count += 1
            star_c += 1
        print(str(count) + "*'s required to balance the string")
    else:
        count = 0
        while hash_c < star_c:
            count += 1
            hash_c += 1
        print(str(count) +"#'s required to balance the string")