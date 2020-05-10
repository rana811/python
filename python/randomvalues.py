# Create a 10x10 array with random values and find minimum and maximum number along axis 1
import numpy as np
x = np.random.random((10,10))
print("Original Array:")
print(x) 
np.amax(x, axis=1)
np.amin(x, axis=1)