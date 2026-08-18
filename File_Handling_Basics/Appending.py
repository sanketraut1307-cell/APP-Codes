# Append data to an existing file

file = open("data.txt", "a")

file.write("\nThis line was added later.")

file.close()

print("Data appended successfully.")

# Output -
# Data appended successfully.
