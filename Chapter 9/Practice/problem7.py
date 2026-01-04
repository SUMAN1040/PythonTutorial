# Write a program to find out the line number where python is present from ques 6


with open("log.txt") as file:
    lines = file.readlines()

lineNo = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present. Line number: {lineNo}")
        break
    lineNo += 1
else:
    print("No python is not present")