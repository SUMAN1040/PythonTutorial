# Check whether a given number is an Armstrong number.
# if __name__ == "__main__":
#     n = int(input("Enter a number: "))

#     if n < 0:
#         print(n, "is not an Armstrong number")
#     else:
#         power = len(str(n))
#         num = n
#         total = 0
#         while num > 0:
#             digit = num % 10
#             total += digit ** power
#             num //= 10

#         if total == n:
#             print(n, "is an Armstrong number")
#         else:
#             print(n, "is not an Armstrong number")




# Check whether a number is a palindrome.
# if __name__ == "__main__":
#     n = int(input("Enter a number: "))
#     num = n
#     reverse = 0
#     while num > 0:
#         digit = num % 10
#         reverse = reverse * 10 + digit
#         num //= 10
#     if reverse == n:
#         print(n, "is a palindrome")
#     else:
#         print(n, "is not a palindrome")




# Check whether a number is prime or composite.
# if __name__ == "__main__":
#     n = int(input("Enter a number: "))
#     if n < 2:
#         print("This is neither prime nor composite")
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 print(n, "is composite number")
#                 break
#         else:
#             print(n, "is prime number")




# Build a menu-driven ATM program with balance checking, deposit and withdrawal.
if __name__ == "__main__":
    balance = 1000.0

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                print(f"Current balance: {balance: 2f}")
            case "2":
                2