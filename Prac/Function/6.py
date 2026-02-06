# def fun(x):
#     while x >= 10:
#         x = x // 10
#     return x

# print(fun(12345))



# Using log base 10 to find the number of digits
import math
def getLastDigits(x):
    d = int(input())
    res = x // (10 ** d)
    return res

print(getLastDigits(12345))




