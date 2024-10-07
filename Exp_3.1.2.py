'''
Date: 06.09.2024
Author: Avinash Singh
Title: Create a 3 x 3 matrix, Identify the values in (0,0) and (2,2). Further, extract the first row, last column and
a 2 x 2 subarray. Perform element-wise operation between two arrays using arithmetic operators. Perform a
broadcasted addition between a matrix and a vector.
'''

#%%

import numpy as np

matrix = np.arange(2, 11).reshape(3, 3)

print("3x3 Matrix:")
print(matrix)

# Identify the values at (0,0) and (2,2)
val00 = matrix[0, 0]
val22 = matrix[2, 2]
print("\nValue at (0,0): {}".format(val00))
print("Value at (2,2): {}".format(val22))

# Extract the first row
first_row = matrix[0, :]
print("\nFirst Row: {}".format(first_row))

# Extract the last column
last_column = matrix[:, -1]
print("Last Column: {}".format(last_column))


topleft2x2 = matrix[0:2, 0:2]
print("\n2x2 Subarray:\n{}".format(topleft2x2))

array_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
elementwise_sum = array_a + array_b
print("\nElement-wise Sum:\n{}".format(elementwise_sum))

vector = np.array([1, 2, 3])
broadcasted_addition = array_a + vector
print("\nBroadcasted Addition Result:\n{}".format(broadcasted_addition))
