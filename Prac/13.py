number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

operator = input("Enter an operator (+, -, *, /): ")

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"
print("The result is:", result)