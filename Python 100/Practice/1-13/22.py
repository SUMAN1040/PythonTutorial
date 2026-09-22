#22. Username Validator

username = input("Enter your username: ")

if 5 <= len(username) <= 15 and username[0].isalpha():
    is_valid = True
    
    for char in username:
        if not (char.isalnum() or char == "_"):
            is_valid = False
            break

    if is_valid:
        print("Valid username")
    else:
        print("Invalid username")
else:
    print("Invalid username")

    