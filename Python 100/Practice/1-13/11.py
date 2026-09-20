#11. Email Extractor

email = input("Enter an email address: ")

username = email.split("@")[0]
domain = email.split("@")[1]

print(f"Username: {username}")
print(f"Domain: {domain}") 