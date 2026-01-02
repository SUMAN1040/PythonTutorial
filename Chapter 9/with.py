f = open("file.txt")
print(f.read())

f.close()


# This same statement can be written using with statement like this:
with open("file.txt") as f:
    print(f.read())

    # By using this , we don't need to explicitly close the file. It will be closed automatically after the nested block of code.