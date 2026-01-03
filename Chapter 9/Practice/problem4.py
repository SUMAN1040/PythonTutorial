# A file contains a word "Donkey" multiple times. you need to write a program which replace this word with ##### by updating the same file.

word = "Donkey"

with open("check_donkey.txt", "r") as file:
    content = file.read()

contentNew = content.replace("Donkey", "#####")

with open("check_donkey.txt", "w") as file:
    file.write(contentNew)

