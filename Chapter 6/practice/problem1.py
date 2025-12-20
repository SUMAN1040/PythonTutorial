number1 = int(input("Enter the number 1: "))
number2 = int(input("Enter the number 2: "))
number3 = int(input("Enter the number 3: "))
number4 = int(input("Enter the number 4: "))

if((number1>= number2) and (number1>=number3) and (number1>=number4)):
    print("Number 1 is the greatest")
elif(number2>=number1 and number2>=number3 and number2>=number4):
    print("Number 2 is the greatest")
elif(number3>=number1 and number3>=number2 and number3>=number4):
    print("Number 3 is the greatest")
else:
    print("Number 4 is the greatest")