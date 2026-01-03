# Repeat program 4 for a list of such words to be censored.

words = ["Donkey", "Bad", "ganda"]

with open("check_donkey.txt", "r") as file:
    content = file.read()

for word in words:
    content = content.replace(word, "@" * len(word))

with open ("check_donkey.txt", "w") as file:
    file.write(content)
