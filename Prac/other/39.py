#Optimize of all divisors and prime factors

#Basic approach
# n = 36
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, end = " ")
# print()


#Optimize Approach
# n = 36
# x = 1

# while x * x <= n:
#     if n % x < n:
#         if n % x == 0:
#             print(x, n // x)
#         x += 1
#     if x * x == n:
#         print(x)


# Checking if a number is prime
# n = 25
# if n <= 1:
#     print(f"For this Number 1")
# for x in range(2, n):
#     if n % x == 0:
#         print("No")
#         break
# else:
#     print("Yes")

# Optimize approach
n = 25
if n <= 1:
    print("No")
else:
    x = 2
    while x * x <= n:
        if n % x == 0:
            print("No")
            break
        x = x + 1
    else:
        print("Yes")