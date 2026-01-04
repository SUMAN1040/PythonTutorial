# Write a python program to rename a file to "renamed_by_python.txt".

with open("old.md") as f:
    content = f.read()

with open("renamed_by_python.md", "w") as f:
    f.write(content)