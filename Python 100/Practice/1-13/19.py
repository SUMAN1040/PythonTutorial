#19. Character Analysis

text = input("Enter a string: ")

total_characters = len(text)
Number_of_vowels = 0
Number_of_consonants = 0
Number_of_space = 0

print(total_characters)

for i in text:
    if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        Number_of_vowels += 1
    elif (i == " "):
        Number_of_space += 1
    else:
        Number_of_consonants += 1

print("Number of vowels: ", Number_of_vowels)
print("Number of consonants: ", Number_of_consonants)
print("Number of spaces: ", Number_of_space)