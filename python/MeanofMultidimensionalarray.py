# Given a Multidimensional array find the following,
#1. What is the average value of the second column
#2. Calculate the Mean of the given Multidimensional array
import numpy as np
array5D = np.array([[174677, 343356, 301717, 224120, 401101],
       [140473, 254634, 112262,  25063, 108262],
       [375059, 406983, 208947, 115641, 296685],
       [444899, 129585, 171318, 313094, 425041],
       [476442,  35455, 191553, 384154,  29917]])
print("Average value of second column  : ", np.average(array5D[...,1])) 
print("Mean of array5D : ", np.average(array5D)) 