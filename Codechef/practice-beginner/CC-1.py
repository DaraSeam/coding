# ATM
# input:
# x: amount of money pooja want to withdraw
# y: the amout of money she has

#output: 
# amount of money she has left her her account after she withdraw

#condition
# x%5==0 and (y-0.50) >= x

# x = 12.50
# format_x = "{:.2f}".format(x)
# print(format_x)
#----------------------------------------------------
x,y = map(float, input().split())

#bruteforce solution
# if x%5 == 0 and (y-0.50) >= x:
#     res = (y-0.50) - x
#     format_res = "{:.2f}".format(res)
#     print(format_res)
# else:
#     format_y = "{:.2f}".format(y)
#     print(format_y)

#optimal solution
print("{:.2f}".format(y-0.50-x)) if (x%5 == 0 and (y-0.50) >= x) else print("{:.2f}".format(y))
