import math
n = int(input())



# By using functions
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
# print(factorial(n))


# By using loop
# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i
# print(fact)


# By using math module
fact = math.factorial(n)
print(fact)
