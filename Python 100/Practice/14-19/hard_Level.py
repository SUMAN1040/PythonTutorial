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
# if __name__ == "__main__":
#     correct_pin = 1234
#     balance = 1000
#     attempts = 0
#     authenticated = False
     
    
#     while attempts < 3:
#         entered_pin = int(input("Enter your PIN: "))
#         if entered_pin == correct_pin:
#             authenticated = True
#             break
#         else:
#             attempts += 1
#             remaining = 3 - attempts
#             if remaining > 0:
#                 print(f"Incorrect PIN! Attempts remaining: {remaining}")
#             else:
#                 print("Card Blocked! Too many incorrect attempts.")
#     # --- Step 2: Menu Loop (runs only if PIN was correct) ---
#     if authenticated:
#         while True:
#             print("\n--- Banking Menu ---")
#             print("1: Check balance")
#             print("2: Deposit cash")
#             print("3: Withdraw cash")
#             print("4: Exit")
#             choice = int(input("Enter your choice: "))
#             if choice == 1:
#                 print(f"Current Balance: ${balance}")
#             elif choice == 2:
#                 amount = int(input("Enter amount to deposit: "))
#                 if amount > 0:
#                     balance += amount
#                     print(f"Deposited successfully. Balance: ${balance}")
#                 else:
#                     print("Invalid amount!")
#             elif choice == 3:
#                 amount = int(input("Enter amount to withdraw: "))
#                 if amount <= 0:
#                     print("Invalid amount!")
#                 elif amount <= balance:
#                     balance -= amount
#                     print(f"Withdrawn successfully. Balance: ${balance}")
#                 else:
#                     print("Insufficient Balance!")
#             elif choice == 4:
#                 print("Thank you for banking with us. Goodbye!")
#                 break
#             else:
#                 print("Invalid choice, please select between 1 and 4.")




# Print all Armstrong numbers between 1 and 10,000.
# if __name__ == "__main__":
#     for num in range(1, 10001):
#         temp = num
#         order = len(str(num))
#         sum = 0
#         while temp > 0:
#             digit = temp % 10
#             sum += digit ** order
#             temp //= 10
#         if sum == num:
#             print(num)




# Print this pyramid pattern for N = 5.
#     *
#    ***
#   *****
#  *******
# *********
# if __name__ == "__main__":
#     n = int(input("Enter the number what need to put: "))
#     for i in range(1, n + 1):
#         # print(" " * (n - i) + "*" * (2 * i - 1))
#         for j in range(n - i):
#             print(" ", end="")
#         for k in range(2 * i - 1):
#             print("*", end="")
#         print()




# Find all pairs of numbers between 1 and 100 whose sum equals a user-provided target.
# if __name__ == "__main__":
#     n = int(input("Enter the target number: "))
    
#     pairs = []

#     for i in range(1, 101):
#         for j in range(i + 1, 101):
#             if i + j == n:
#                 pairs.append((i, j))
    
#     print(pairs)




# Convert a decimal number into binary without using Python's built-in bin() function.
# if __name__ == "__main__":
#     n = int(input("Enter the decimal number: "))
#     binary = ""
#     while n > 0:
#         r = n % 2
#         binary = str(r) + binary
#         n = n // 2
#     print(binary)




# Find the first 5 prime numbers greater than 100 using while, break and continue.
# if __name__ == "__main__":
#     count = 0
#     num = 101
#     while count < 5:
#         is_prime = True
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num)
#             count += 1
#         num += 1




# Create a menu-driven number analyzer that can check prime, palindrome, Armstrong, perfect number and reverse a number. Keep showing the menu until the user selects Exit.
if __name__ == "__main__":
    while True:
        print("\n--- Number Analyzer ---")
        print("1: Check Prime")
        print("2: Check Palindrome")
        print("3: Check Armstrong")
        print("4: Check Perfect")
        print("5: Reverse a Number")
        print("6: Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            num = int(input("Enter the number: "))
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print("Prime")
            else:
                print("Not Prime")
        elif choice == 2:
            num = int(input("Enter the number: "))
            temp = num
            reverse = 0
            while temp > 0:
                r = temp % 10
                reverse = reverse * 10 + r
                temp = temp // 10
            if num == reverse:
                print("Palindrome")
            else:
                print("Not Palindrome")
        elif choice == 3:
            num = int(input("Enter the number: "))
            temp = num
            order = len(str(num))
            sum = 0
            while temp > 0:
                digit = temp % 10
                sum += digit ** order
                temp //= 10
            if sum == num:
                print("Armstrong")
            else:
                print("Not Armstrong")
        elif choice == 4:
            num = int(input("Enter the number: "))
            sum = 0
            for i in range(1, num):
                if num % i == 0:
                    sum += i
            if sum == num:
                print("Perfect")
            else:
                print("Not Perfect")
        elif choice == 5:
            num = int(input("Enter the number: "))
            temp = num
            reverse = 0
            while temp > 0:
                r = temp % 10
                reverse = reverse * 10 + r
                temp = temp // 10
            print(reverse)
        elif choice == 6:
            break
        else:
            print("Invalid choice")
            