import numpy as np

a = np.array([[3, 6], [9, 12]])
b = np.array([[1, 2], [3, 4]])

print("a * b:\n", a * b)
print("a / 3:\n", a / 3)
print("Sum of a:", np.sum(a))
print("Sqrt of b:\n", np.sqrt(b))
print("Transpose of a:\n", a.T)

c = np.array([["x", "y"], ["z", "w"]])
print("String array c:\n", c)
print("Type of c:", c.dtype)
