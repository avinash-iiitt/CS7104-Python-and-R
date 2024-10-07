'''
Date: 06.09.2024
Author: Avinash Singh
Title: Write a python script to create a 2D NumPy array having random numbers from 1 to 100. Find the
maximum, minimum, sum and mean of the array.
'''

#%%

import numpy as np

rows, cols = 5, 5
array_2d = np.random.randint(1, 101, size=(rows, cols))

# Display the array
print("2D Array:")
print(array_2d)

# Calculate maximum, minimum, sum, and mean
max_val = np.max(array_2d)
min_val = np.min(array_2d)
sum_val = np.sum(array_2d)
mean_val = np.mean(array_2d)


print("\nResults:")
print("Maximum: {}".format(max_val))
print("Minimum: {}".format(min_val))
print("Sum: {}".format(sum_val))
print("Mean: {}".format(round(mean_val,2)))
