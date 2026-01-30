# Print a table of any number

num = int(input("Enter a number to print its table: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")