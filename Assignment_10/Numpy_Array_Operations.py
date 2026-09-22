import numpy as np

# Create array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Array:", arr)

# Slicing
print("First 5:", arr[:5])
print("Even positions:", arr[1::2])

# Statistical measures
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Broadcasting
arr = arr + 5
print("After broadcasting:", arr)

# Output - 
# Array: [ 1  2  3  4  5  6  7  8  9 10]
# First 5: [1 2 3 4 5]
# Even positions: [ 2  4  6  8 10]
# Sum: 55
# Mean: 5.5
# Maximum: 10
# Minimum: 1
# After broadcasting: [ 6  7  8  9 10 11 12 13 14 15]
