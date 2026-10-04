import pandas as pd
import numpy as np

# Create a Series containing 10 random numbers
series = pd.Series(np.random.randint(1, 101, 10))

print("Original Series:")
print(series)

# Indexing
print("\nIndexing:")
print("First element:", series[0])
print("Fifth element:", series[4])

# Filtering
print("\nFiltering (Numbers greater than 50):")
print(series[series > 50])

# Statistical Operations
print("\nStatistical Operations:")
print("Mean:", series.mean())
print("Median:", series.median())
print("Minimum:", series.min())
print("Maximum:", series.max())

Comment:-
Original Series:
0    23
1    78
2    45
3    91
4    12
5    67
6    34
7    88
8    56
9    29
dtype: int64

Indexing:
First element: 23
Fifth element: 12

Filtering (Numbers greater than 50):
1    78
3    91
5    67
7    88
8    56
dtype: int64

Statistical Operations:
Mean: 52.3
Median: 50.5
Minimum: 12
Maximum: 91
