a = int(input("Enter your age: "))
# print("Your age is: ", a)

#Conditional Operators (>, <, >=, <=, ==, !=)
if a > 18:
    print("You can drive")
else:
    print("You can't drive")

#Nested Loop
num = 18
if (num < 0):
    print("Number is negetive")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is 0")