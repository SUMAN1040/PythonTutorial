#16. Password Masking
password = input("Enter your password: ")

masked = "*" * len(password)

print(masked)

if len(password) <= 2:
    masked = password
else:
    masked = "*" * (len(password) - 2) + password[-2:]

print(masked)