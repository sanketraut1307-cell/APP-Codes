import numpy as np
import pandas as pd

# Employee details
names = ["Amit", "Rahul", "Sneha", "Priya", "Rohit"]

# Create NumPy array of salaries
salaries = np.array([45000, 65000, 75000, 55000, 85000])

# Calculate salary statistics
average_salary = np.mean(salaries)
maximum_salary = np.max(salaries)
minimum_salary = np.min(salaries)

print("Average Salary:", average_salary)
print("Maximum Salary:", maximum_salary)
print("Minimum Salary:", minimum_salary)

# Create Pandas DataFrame
df = pd.DataFrame({
    "Employee": names,
    "Salary": salaries
})

print("\nEmployee Salary Data:")
print(df)

# Display employees earning more than ₹60,000
print("\nEmployees earning more than ₹60,000:")
print(df[df["Salary"] > 60000])

# # Output - 
# Average Salary: 65000.0
# Maximum Salary: 85000
# Minimum Salary: 45000

# Employee Salary Data:
#   Employee  Salary
# 0     Amit   45000
# 1    Rahul   65000
# 2    Sneha   75000
# 3    Priya   55000
# 4    Rohit   85000

# Employees earning more than ₹60,000:
#   Employee  Salary
# 1    Rahul   65000
# 2    Sneha   75000
# 4    Rohit   85000
