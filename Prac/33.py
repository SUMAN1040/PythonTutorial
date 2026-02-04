#Using the math module to perform mathematical operations

# import math

# n = 5

# print(math.factorial(n))  # Output: 120


#Using Numpy module

# import numpy as np
# n = 5
# print(np.prod(range(1, n + 1)))


#Using iterative loop
# n = 6
# f = 1

# for i in range(1, n + 1):
#     f *= i

# print(f)  # Output: 720


#Using recursive function
# def fact(n):
#     return 1 if n <= 1 else n * fact(n - 1)
# print(fact(6))  # Output: 720