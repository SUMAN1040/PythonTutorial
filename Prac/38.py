# All divisors of A number
# n = 12
# for x in range(1, n + 1):
#     if n % x == 0:
#         print(x, end=' ')
# print()


#Using while loop
n = 12
x = 1
while x <= n:
    if n % x == 0:
        print(x, end=' ')
    x += 1
print()