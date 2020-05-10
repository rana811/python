#11 For the given array, get the slice of the first row and display them
import numpy as np
array2 = np.array([[[22, 23, 24], [25, 26, 27], [28, 29, 30]],
               [[31, 32, 33], [34, 35, 36], [37, 38, 39]],
               [[40, 41, 42], [43, 44, 45], [46, 47, 48]]])

b = array2[:,:1,:]

print(b)