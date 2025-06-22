import numpy as np 

#Iteration

#ndim =1
arr = np.array([1, 2, 3])

for x in arr:
  print(x) 

#ndim = 2
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x) 

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y) 

#nditer
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x) 