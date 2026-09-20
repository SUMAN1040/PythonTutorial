#5. Simple Interest
principle = float(input("Enter the pricicple ammount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))

print(f" The total ammount: {principle * rate * time / 100}")