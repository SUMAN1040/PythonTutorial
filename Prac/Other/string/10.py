# def binToDec(b):
#     res = 0
#     p = 1
#     for i in reversed(b):
#         res = res + int(i)*p
#         p = p * 2
#     return res
# print(binToDec('1100'))

def binToDec(b):
    res = int(b, 2)
    return res
print(binToDec('1100'))

