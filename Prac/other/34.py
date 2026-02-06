#GCD in python

# import math

# a = 60
# b = 48

# print(math.gcd(a, b))


# GCD of two co-prime numbers
# import math

# print(math.gcd(17, 29))


# GCD in a list of numbers using functools.reduce()
import math
from functools import reduce

nums = [48, 64, 80]

# Find GCD of the list
res = reduce(math.gcd, nums)
print(res)