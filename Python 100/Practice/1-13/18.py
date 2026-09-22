#18. Reverse Words

text = input("Enter the word:")

word = text.split()

reversed_text = word[::-1]

result = " ".join(reversed_text)

print(f"The reversed words are: {result}")

