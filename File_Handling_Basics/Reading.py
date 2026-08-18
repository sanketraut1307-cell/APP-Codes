# Read data from a file

file = open("data.txt", "r")

data = file.read()

print("File Content:")
print(data)

file.close()

# Output - 
# File Content:
# Hello, this is my first file.
# I am learning Python file handling.
