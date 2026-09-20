#3. Temperature Converter

temparature = float(input("Enter the temparature: "))
unit = input("Enter the temp unit(F / C): ")

if unit == "F" or unit == "f":
    print(f"{temparature - 32 * (5 / 9):.2f} C")
elif unit == "C" or unit == "c":
    print(f"{temparature * (9 / 5) + 32:.2f} F")
else:
    print("Invalid Unit")