import numpy as np

arr1 = np.array(['x', 'y', 'z']); print("String Array:", arr1)

arr2 = np.array([[1.1, 2.2], [3.3, 4.4]]); print("Float Array:\n", arr2)

print("Slice row 1:", arr2[1])
print("Slice col 0:", arr2[:, 0])
