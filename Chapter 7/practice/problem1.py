# Write a program to print multiplication table of the given number using for loop.

num = int(input("Enter the number:"))

for i in range(1, 11):
    print(f"{num} * {i} = {num*i}")