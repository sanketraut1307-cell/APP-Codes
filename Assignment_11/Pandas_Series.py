import pandas as pd
import numpy as np

# Create a Series containing 10 random numbers
s = pd.Series(np.random.randint(1, 100, 10))

print("Series:")
print(s)

# Indexing
print("\nValue at index 2:", s[2])

# Filtering
print("\nNumbers greater than 50:")
print(s[s > 50])

# Statistical operations
print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())

(* Output - 
Series:
0    23
1    67
2    45
3    89
4    12
5    56
6    34
7    78
8    91
9    40
dtype: int64

Value at index 2: 45

Numbers greater than 50:
1    67
3    89
5    56
7    78
8    91
dtype: int64

Mean: 53.5
Median: 50.5
Minimum: 12
Maximum: 91 *)
