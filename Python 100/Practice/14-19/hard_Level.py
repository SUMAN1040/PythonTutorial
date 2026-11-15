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
    correct_pin = 1234
    balance = 1000
    attempts = 0
    authenticated = False
     
    
    while attempts < 3:
        entered_pin = int(input("Enter your PIN: "))
        if entered_pin == correct_pin:
            authenticated = True
            break
        else:
            attempts += 1
            remaining = 3 - attempts
            if remaining > 0:
                print(f"Incorrect PIN! Attempts remaining: {remaining}")
            else:
                print("Card Blocked! Too many incorrect attempts.")
    # --- Step 2: Menu Loop (runs only if PIN was correct) ---
    if authenticated:
        while True:
            print("\n--- Banking Menu ---")
            print("1: Check balance")
            print("2: Deposit cash")
            print("3: Withdraw cash")
            print("4: Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print(f"Current Balance: ${balance}")
            elif choice == 2:
                amount = int(input("Enter amount to deposit: "))
                if amount > 0:
                    balance += amount
                    print(f"Deposited successfully. Balance: ${balance}")
                else:
                    print("Invalid amount!")
            elif choice == 3:
                amount = int(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Invalid amount!")
                elif amount <= balance:
                    balance -= amount
                    print(f"Withdrawn successfully. Balance: ${balance}")
                else:
                    print("Insufficient Balance!")
            elif choice == 4:
                print("Thank you for banking with us. Goodbye!")
                break
            else:
                print("Invalid choice, please select between 1 and 4.")