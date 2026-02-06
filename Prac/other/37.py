# n = 11

# if n <= 1:
#     print("Not prime")
# else:
#     is_prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#             break
#     print(is_prime)


# from sympy import *

# g1 = isprime(11)
# print(g1)



# Using sieve of Eratosthenes to find all prime numbers up to n

# def is_prime(n):
#     if n < 2:
#         return False

#     sieve = [True] * (n + 1)
#     sieve[0] = sieve[1] = False

#     for i in range(2, int(n**0.5) + 1):
#         if sieve[i]:
#             for j in range(i * i, n + 1, i):
#                 sieve[j] = False

#     return sieve[n]


# num = 31
# print(is_prime(num))


# Using recursion
from math import sqrt

def Prime(n, i):  
    if i == 1 or i == 2:  
        return True
    if n % i == 0:  
        return False

    return Prime(n, i - 1)

n = 13
i = int(sqrt(n) + 1)

print(Prime(n, i))