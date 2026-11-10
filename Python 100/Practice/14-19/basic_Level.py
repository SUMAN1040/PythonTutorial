# Write a program to check whether a number is positive, negative or zero.

# if __name__ == "__main__":
#     num = float(input("Enter a number: "))
#     if num > 0:
#         print("The number is positive")
#     elif num < 0:
#         print("The number is negative")
#     else:
#         print("The number is zero")





# Check whether a number is even or odd.

# if __name__ == "__main__":
#     num = float(input("Enter a number:"))
#     if num % 2 == 0:
#         print("The number is even")
#     else:
#         print("The number is odd")





# Take age as input and check whether a person is eligible to vote (18+).
# if __name__ == "__main__":
#     age = float(input("Enter your age: "))
#     if age >= 18:
#         print("This person can vote")
#     else:
#         print("This person age not eligible for vote")





# Find the greater of two numbers.
# if __name__ == "__main__":
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))

#     if num1 > num2:
#         print(f"{num1} is greater than {num2}")
#     else:
#         print(f"{num2} is greater than {num1}")




# Create a calculator using match-case for addition, subtraction, multiplication and division.
# if __name__ == "__main__":
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
    
#     choice = input("Enter the operation(+, -, *, /): ")
#     match choice:
#         case "+":
#             print(f"Result: {num1 + num2}")
#         case "-":
#             print(f"Result: {num1 - num2}")
#         case "*":
#             print(f"Result: {num1 * num2}")
#         case "/":
#             if num2 == 0:
#                 print("Denominator can't be zero")
#             else:
#                 print(f"Result: {num1/num2}")
#         case _:
#             print("Invalid choice")




# Print numbers from 1 to 20 using a for loop.
# if __name__ == "__main__":
#     for i in range(20):
#         print(i + 1)




# # Print the multiplication table of a number entered by the user.
# if __name__ == "__main__":
#     num = int(input("Enter a number:"))
#     for i in range(1, 11):
#         print(f"{num} * {i} : {num*i}")




# Print numbers from 10 to 1 using a while loop.
# if __name__ == "__main__":
#     num = 10
#     while num >= 1:
#         print(num)
#         num -= 1




# Calculate the sum of numbers from 1 to N.
# if __name__ == "__main__":
#     num = int(input("Enter the number: "))
#     sum = 0
#     for i in range(1, num + 1):
#         sum += i
#     print(f"The sum of numbers from 1 to {num} is: {sum}")




# Print numbers from 1 to 20 but stop when the number reaches 12.

# if __name__ == "__main__":
#     for i in range(1, 21):
#         if i == 12:
#             break
#         print(i)