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
# if __name__ == "__main__":
#     balance = 1000.0

#     while True:
#         print("\n--- ATM Menu ---")
#         print("1. Check Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exit")

#         choice = input("Enter your choice (1-4): ")

#         match choice:
#             case "1":
#                 print(f"Current balance: {balance:.2f}")
#             case "2":
#                 amount = float(input("Enter amount to deposit: "))
#                 if amount > 0:
#                     balance += amount
#                     print(f"Deposited {amount:.2f}. New balance: {balance:.2f}")
#                 else:
#                     print("Deposit amount must be positive.")
#             case "3":
#                 amount = float(input("Enter amount to withdraw: "))
#                 if amount <= 0:
#                     print("Withdrawal amount must be positive.")
#                 elif amount > balance:
#                     print("Insufficient balance!")
#                 else:
#                     balance -= amount
#                     print(f"Withdrew {amount:.2f}. Remaining balance: {balance:.2f}")
#             case "4":
#                 print("Thank you for using the ATM. Goodbye!")
#                 break
#             case _:
                # print("Invalid choice. Please select 1-4.")




# Build a simple unit converter (kilometres/miles, Celsius/Fahrenheit, kg/pounds).
# if __name__ == "__main__":
#     amount = float(input("Enter the amount to be converted: "))

#     print("\n--- Unit Converter ---")
#     print("1. Kilometres to Miles")
#     print("2. Miles to Kilometres")
#     print("3. Celsius to Fahrenheit")
#     print("4. Fahrenheit to Celsius")
#     print("5. Kilograms to Pounds")
#     print("6. Pounds to Kilograms")

#     choice = input("Choose conversion (1-6): ")

#     match choice:
#         case "1":
#             print(f"{amount} km = {amount * 0.621371:.2f} miles")
#         case "2":
#             print(f"{amount} miles = {amount / 0.621371:.2f} km")
#         case "3":
#             print(f"{amount} °C = {(amount * 9 / 5) + 32:.2f} °F")
#         case "4":
#             print(f"{amount} °F = {(amount - 32) * 5 / 9:.2f} °C")
#         case "5":
#             print(f"{amount} kg = {amount * 2.20462:.2f} lbs")
#         case "6":
#             print(f"{amount} lbs = {amount / 2.20462:.2f} kg")
#         case _:
#             print("Invalid choice. Please select 1-6.")




# Print the following pattern for N = 5.
# *
# **
# ***
# ****
# *****
# if __name__ == "__main__":
#     n = int(input("Enter a number: "))
#     for i in range(1, n + 1):
#         print("*" * i)




# Print all prime numbers between 1 and 100.
# if __name__ == "__main__":
#     for i in range(2, 101):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             print(i, end=" ")
#     print()




# Generate the Fibonacci series up to N terms.
# if __name__ == "__main__":
#     n = int(input("Enter the number of terms: "))
#     a, b = 0, 1
#     print("Fibonacci series:", end=" ")
#     while a < n:
#         print(a, end=" ")
#         a, b = b, a + b




# Take 10 numbers from the user. Stop immediately if the user enters 0. Skip negative numbers and calculate the sum of positive numbers.
if __name__ == "__main__":
    total = 0
    count = 0
    for i in range(10):
        num = int(input("Enter a number: "))
        if num == 0:
            break
        if num < 0:
            continue
        total += num
        count += 1
    print("Sum:", total)