import numpy as np

arr1 = np.array([10, 20, 30]); print("Array 1:", arr1)

arr2 = np.array([[1, 2], [3, 4]]); print("Array 2:\n", arr2)

arr3 = np.array([(7, 8), (9, 10)]); print("Array 3:\n", arr3)

arr4 = np.array([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
print("Sliced Rows:\n", arr4[1:, :])
print("Sliced Cols:\n", arr4[:, ::2])cl