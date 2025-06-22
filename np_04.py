import numpy as np

#split
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

#split_array

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2]) 

#2d
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)

#search

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

#odd
arr = np.array([1, 2, 3, 4])

x = np.where(arr%2 == 1)

print(x) 
#even

arr = np.array([1, 2, 3, 4, 5])

x = np.where(arr%2 == 0)

print(x) 