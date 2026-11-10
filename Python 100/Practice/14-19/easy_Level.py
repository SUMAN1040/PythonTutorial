# Find the largest among three numbers.
# if __name__ == "__main__":
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     num3 = int(input("Enter the third number: "))
#     largest = num1
#     if num2 > largest:
#         largest = num2
#     if num3 > largest:
#         largest = num3
#     print(f"The largest number is: {largest}")\




# Check whether a year is a leap year.
# if __name__ == "__main__":
#     year = int(input("Enter the year:"))
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not a leap year")




# Create a grading system: 90+ A, 80+ B, 70+ C, 60+ D, below 60 F.
# if __name__ == "__main__":
#     score = int(input("Enter your score: "))
#     if score >= 90:
#         print("Grade: A")
#     elif score >= 80:
#         print("Grade: B")
#     elif score >= 70:
#         print("Grade: C")
#     elif score >= 60:
#         print("Grade: D")
#     else:
#         print("Grade: F")




# Create a program that accepts a day number (1–7) and prints the day name.
# if __name__ == "__main__":
#     day = int(input("Enter the day number(1-7): "))
#     choice = {
#         1:"Monday",
#         2:"Tuesday",
#         3:"Wednesday",
#         4:"Thursday",
#         5:"Friday",
#         6:"Saturday",
#         7:"Sunday"
#     }

#     if day in choice:
#         print(f"The day is {choice[day]}")
#     else:
#         print(f"{day} is not a valid day number")




# Create a menu-driven program for calculating the area of a circle, rectangle and square.
# if __name__ == "__main__":
#     choice = int(input("Choose an option(1:Area of circle,2:Area of rectangle,3:Area of square): "))

#     if choice == 1:
#         radius = float(input("Enter the radius: "))
#         area = 3.14 * radius * radius
#         print(f"The area of the circle is: {area}")

#     elif choice == 2:
#         length = float(input("Enter the length: "))
#         width = float(input("Enter the width: "))
#         area = length * width
#         print(f"The area of the rectangle is: {area}")

#     elif choice == 3:
#         side = float(input("Enter the side: "))
#         area = side * side
#         print(f"The area of the square is: {area}")

#     else:
#         print("Invalid choice")




# Calculate the factorial of a number using a for loop.
# if __name__ == "__main__":
#     num = int(input("Enter the number:"))
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial *= i
#     print(f"The factorial of {num} is {factorial}")  




# Count how many even and odd numbers exist between 1 and 100.
# if __name__ == "__main__":
#     even = 0
#     odd = 0
#     for i in range(1, 101):
#         if i % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     print(f"Odd count: {odd}")
#     print(f"Even count: {even}")




# Reverse a given number. Example: 1234 → 4321.
# if __name__ == "__main__":
#     num = int(input("Enter the number: "))

#     reverse_number = 0
#     while num > 0:
#         remainder = num % 10
#         reverse_number = (reverse_number * 10) + remainder
#         num = num // 10

#     print(f"The reverse of the number is: {reverse_number}")




# Count the number of digits in an integer.
# if __name__ == "__main__":
#     num = int(input("Enter the number: "))
#     count = 0
#     while num > 0:
#         num //= 10
#         count += 1
#     print(f"The number of digits is {count}")




# Print numbers from 1 to 30 but skip all multiples of 3.
if __name__ == "__main__":
    for i in range(1, 31):
        if i % 3 == 0:
            continue
        print(i)