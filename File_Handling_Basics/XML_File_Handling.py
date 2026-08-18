import xml.etree.ElementTree as ET

# Create XML data
root = ET.Element("student")

name = ET.SubElement(root, "name")
name.text = "Sanket"

age = ET.SubElement(root, "age")
age.text = "20"

city = ET.SubElement(root, "city")
city.text = "Pune"

# Write to XML file
tree = ET.ElementTree(root)
tree.write("student.xml")

# Read XML file
tree = ET.parse("student.xml")
root = tree.getroot()

print("Student Details:")
print("Name:", root.find("name").text)
print("Age:", root.find("age").text)
print("City:", root.find("city").text)

# Output - 
# Student Details:
# Name: Sanket
# Age: 20
# City: Pune
