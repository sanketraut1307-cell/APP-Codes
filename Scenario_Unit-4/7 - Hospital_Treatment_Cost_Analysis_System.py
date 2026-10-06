import numpy as np
import pandas as pd

# Patient details
patients = ["Amit", "Rahul", "Sneha", "Priya", "Rohit"]

# Create NumPy array of treatment costs
costs = np.array([15000, 25000, 18000, 30000, 22000])

# Calculate treatment cost statistics
mean_cost = np.mean(costs)
maximum_cost = np.max(costs)
minimum_cost = np.min(costs)

print("Mean Treatment Cost:", mean_cost)
print("Maximum Treatment Cost:", maximum_cost)
print("Minimum Treatment Cost:", minimum_cost)

# Create Pandas DataFrame
df = pd.DataFrame({
    "Patient": patients,
    "Treatment Cost": costs
})

print("\nPatient Treatment Cost Data:")
print(df)

# Display patients whose treatment cost exceeds ₹20,000
print("\nPatients with treatment cost above ₹20,000:")
print(df[df["Treatment Cost"] > 20000])

# # Output - 
# Mean Treatment Cost: 22000.0
# Maximum Treatment Cost: 30000
# Minimum Treatment Cost: 15000

# Patient Treatment Cost Data:
#   Patient  Treatment Cost
# 0    Amit           15000
# 1   Rahul           25000
# 2   Sneha           18000
# 3   Priya           30000
# 4   Rohit           22000

# Patients with treatment cost above ₹20,000:
#   Patient  Treatment Cost
# 1   Rahul           25000
# 3   Priya           30000
# 4   Rohit           22000
