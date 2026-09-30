import numpy as np

# Create a one-dimensional array from 1 to 10
arr = np.arange(1, 11)

print("Original Array:")
print(arr)

# Slicing operations
print("\nFirst 5 elements:")
print(arr[:5])

print("\nElements from index 5 to 9:")
print(arr[5:])

print("\nAlternate elements:")
print(arr[::2])

# Statistical measures
print("\nSum of array:", np.sum(arr))
print("Mean of array:", np.mean(arr))
print("Maximum value:", np.max(arr))
print("Minimum value:", np.min(arr))

# Broadcasting
# Add 5 to every element of the array
arr = arr + 5

print("\nArray after broadcasting (adding 5):")
print(arr)

Comments:-
Original Array:
[ 1  2  3  4  5  6  7  8  9 10]

First 5 elements:
[1 2 3 4 5]

Elements from index 5 to 9:
[ 6  7  8  9 10]

Alternate elements:
[1 3 5 7 9]

Sum of array: 55
Mean of array: 5.5
Maximum value: 10
Minimum value: 1

Array after broadcasting (adding 5):
[ 6  7  8  9 10 11 12 13 14 15]
