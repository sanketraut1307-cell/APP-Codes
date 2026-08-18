import json

data = {
    "name": "Sanket",
    "age": 20,
    "city": "Pune"
}

# Write data to JSON
with open("student.json", "w") as file:
    json.dump(data, file, indent=4)

# Read data from JSON
with open("student.json", "r") as file:
    student = json.load(file)

print("Student Details:")
print("Name:", student["name"])
print("Age:", student["age"])
print("City:", student["city"])

# Output - 
# Student Details:
# Name: Sanket
# Age: 20
# City: Pune
