# Iterative Division
# def get_first_digit(x):
#     while x >= 10:
#         x = x // 10
#     return x


# # Example usage
# number = 7549
# first_digit = get_first_digit(number)
# print("The first digit is:", first_digit)



#Using Logarithms Function
import math


def get_first_digit_log(x):
    d = int(math.log10(x))  # Total number of digits minus 1
    return x // 10**d


# Example usage
number = 7549
first_digit = get_first_digit_log(number)
print("The first digit is:", first_digit)