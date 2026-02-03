num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

res = max(num1, num2)

while (res <= num1 * num2):
    if (res % num1 == 0 and res % num2 == 0):
        print(f"The LCM of {num1} and {num2} is {res}")
        break
    res += 1