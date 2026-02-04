# Find the LCM of Two Numbers Using Loop
# def LCM(a, b):
#     greater = max(a, b)
#     smallest = min(a, b)
#     for i in range(greater, a*b+1, greater):
#         if i % smallest == 0:
#             return i

# # Driver program to test above function
# if __name__ == '__main__':
#     a = 12
#     b = 15
#     print("LCM of", a, "and", b, "is", LCM(a, b))



# Find LCM of Two Numbers Using the GCD (Greatest Common Divisor)

# import math

# def lcm_using_gcd(a, b):
#     gcd = math.gcd(a, b)
#     lcm = (a * b) // gcd
#     return lcm

# # Example usage:
# num1 = 12
# num2 = 15
# print("LCM of", num1, "and", num2, "is:", lcm_using_gcd(num1, num2))


# Find LCM of Two Numbers Using Prime Factorization
def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def lcm_using_prime_factors(a, b):
    factors_a = prime_factors(a)
    factors_b = prime_factors(b)
    lcm = 1
    for factor in set(factors_a + factors_b):
        lcm *= factor ** max(factors_a.count(factor), factors_b.count(factor))
    return lcm

# Example usage:
num1 = 12
num2 = 15
print("LCM of", num1, "and", num2, "is:", lcm_using_prime_factors(num1, num2))