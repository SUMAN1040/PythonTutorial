num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# small = min(num1, num2)

# for i in range(1, small + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i
# print("GCD is:", gcd)


# By using math module
import math
gcd = math.gcd(num1, num2)
print("GCD is:", gcd)