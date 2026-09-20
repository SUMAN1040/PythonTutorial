#13. Count a Character
sentence = input("Enter your sentence: ")

char = input("Enter the character to count: ")

count = 0

for i in sentence:
    if i == char:
        count +=1

print(count)