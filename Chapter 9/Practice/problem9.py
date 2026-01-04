# Write a problem to find out whether a file is identical & matches the content of another file

with open("copy.txt") as f:
    content1 = f.read()

with open("this.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("The files are identical.")
else:
    print("The files are not identical.")