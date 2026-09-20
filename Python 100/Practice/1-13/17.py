#17. Palindrome Checker
text = input("Enter a string: ")

cleaned = text.lower()

if cleaned == cleaned[::-1]:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")