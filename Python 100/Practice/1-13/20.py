#20. Name Initial Generator

name = input("Enter your full name: ")

word = name.split()

initials = ""

for i in word:
    initials = initials + i[0].upper()

print(".".join(initials))