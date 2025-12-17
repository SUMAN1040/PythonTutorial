# Invoke os to read and list files in root directory
import os

#Specify the directory path
directory_path = '/'

#List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each item in the directory
print(contents)