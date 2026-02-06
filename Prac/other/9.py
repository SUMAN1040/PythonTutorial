a = int(input("Enter the number: "))

if a > 0: 
    if a % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
elif a < 0:
    if a % 2 == 0:
        print("Negative even number")
    else:
        print("Negative odd number")
else:
    print("Zero is neither positive nor negative")