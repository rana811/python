# Given a Multidimensional array find the following,
#1. get second and third coloum from the given Multidimensional array
#2.get second and third row from the given Multidimensional array
#3. and reverse the given Multidimensional array
import numpy as np
arr = np.array([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])
print(arr[:, 1],arr[:,2])
print(arr[1,:],arr[2,:])
print("Reverse array:")
arr = arr[::-1]
print(arr)