# From the given array [[ 0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9, 10, 11]] form an array containing elements greater than 5
import numpy as np
x = np.array([[ 0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9, 10, 11]])
print("Original array: ")
print(x)
print("Values bigger than 5 =", x[x>5])