# def fun():
#     print("Hello World")

# print("This is a function example.")
# fun()
# print("Function execution completed.")



# def printDate(d, m, y):
#     print(f"{d}/{m}/{y}")


# print("Enter the date (dd mm yyyy): ")
# printDate(12, 5, 2024)




def fun(d, m, y):
    return d + "-" + m + "-" + y

print("Enter the date (dd mm yyyy): ")
date = fun("12", "05", "2024")
print("Formatted date:", date)