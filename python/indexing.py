# Get [1, 4, 5] from [[1, 2], [3, 4], [5, 6]] using indexing
import numpy as np
def extract(a_list):
    return a_list[0][0],a_list[1][1],a_list[2,0]
arraylist = np.array([[1,2],[3,4],[5,6]])
print(extract(arraylist))