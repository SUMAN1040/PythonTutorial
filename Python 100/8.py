number1 = int(input("Enter First Number:"))
number2 = int(input("Enter Second Number:"))

Operator = input("Enter Operator (+, -, *, /):")

if Operator == "+":
    print(number1 + number2)
elif Operator == "-":
    print(number1 - number2)
elif Operator == "*":
    print(number1 * number2)
elif Operator == "/":
    print(number1 / number2)
else:
    print("Invalid Operator")