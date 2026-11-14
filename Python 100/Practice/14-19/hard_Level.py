# Write a program to check whether a number is a Strong Number. Example: 145 = 1! + 4! + 5!.
# if __name__ == "__main__":
#     num = int(input("Enter the number: "))
#     tst = num

#     count = 0

#     while tst > 0:
#         r = tst % 10
#         fact = 1
#         for i in range(1, r+1):
#             fact = fact * i
#         count += fact
#         tst = tst // 10
#     if num > 0 and count == num:
#         print("Strong Number")
#     else:
#         print("Not a Strong Number")




# Check whether a number is a Perfect Number. Example: 28 = 1 + 2 + 4 + 7 + 14.
# if __name__ == "__main__":
#     num = int(input("Enter the number: "))
#     sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             sum += i

#     if num > 0 and sum == num:
#         print("Perfect Number")
#     else:
#         print("Not a Perfect Number")




# Build a menu-driven banking system with PIN verification, balance inquiry, deposit, withdrawal and exit. Allow a maximum of 3 incorrect PIN attempts.
if __name__ == "__main__":
    pin = 1234
    print("Please insert your pin: ")
    count = 0

    while count < 3:
        

