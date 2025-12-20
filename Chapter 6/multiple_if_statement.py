a = int(input("Enter a number: "))

#if elif else ladder

if(a%2==0):
    print("The number is even")

if(a>=18):
    print("You are above the age of 18")
    print("You are eligible to vote")

elif(a<0):
    print("You have entered an invalid age")

elif(a == 0):
    print("You have entered zero as your age")

else:
    print("You are below the age of 18")

print("Thank you!")