def inchToCm(inch):
    return inch*2.54

n = int(input("Enter the value in inches: "))
print(f"The corresponding value in cms in {inchToCm(n)}")