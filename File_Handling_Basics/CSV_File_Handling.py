import csv

# Write data to CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Sanket", 20, "Pune"])
    writer.writerow(["Rahul", 21, "Mumbai"])

# Read data from CSV
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    print("Student Details:")
    for row in reader:
        print(row)

# Output - 
# Student Details:
# ['Name', 'Age', 'City']
# ['Sanket', '20', 'Pune']
# ['Rahul', '21', 'Mumbai']
