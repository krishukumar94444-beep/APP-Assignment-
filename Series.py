import pandas as pd

# Create Series
data = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(data)

# Update elements
s = pd.Series([100, 200, 300], index=['x', 'y', 'z'])

s['y'] = 500
s[['x', 'z']] = [111, 999]

print(s)

# Convert Series
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

list_data = s.tolist()
dict_data = s.to_dict()
array_data = s.to_numpy()

print("\n \n List:", list_data)
print("Dictionary:", dict_data)
print("NumPy Array:", array_data)

# Sorting
s = pd.Series([40, 10, 30, 20], index=['d', 'a', 'c', 'b'])

sorted_values = s.sort_values()
sorted_index = s.sort_index()

print("Sorted by Values:")
print(sorted_values)

print("\nSorted by Index:")
print(sorted_index)
