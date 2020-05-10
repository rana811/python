#16 Compute  ex , element-wise for a sample array
import numpy as np
x = np.array([1., 2., 3., 4.,5.], np.float32)
print("Original array: ")
print(x)
print("\ne^x, element-wise:")
r = np.exp(x)
print(r)
