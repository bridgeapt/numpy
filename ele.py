import numpy as np

# 1D array (just a single row of numbers)
arr1 = np.array([10, 20, 30, 40])
print("1D Array:", arr1)
print("First element:", arr1[0])
print("Last element:", arr1[-1])

print("\n")

# 2D array (rows and columns like a table)
arr2 = np.array([[1, 2], [3, 4]])
print("2D Array:\n", arr2)
print("Element at row 0, col 1:", arr2[0, 1])
print("Second row:", arr2[1])
