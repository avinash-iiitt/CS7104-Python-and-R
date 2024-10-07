'''
Date: 06.09.2024
Author: Avinash Singh
Title: Create two lambda functions and compose them to manually perform a square followed by an increment by
stepsize 1.
'''

#%%

# creating lambda function to calculate the square
square = lambda x: x ** 2

# creating a lambda function to increment value by 1
increment = lambda x: x + 1

# calling both the lambda functions
square_and_inc1 = lambda x: increment(square(x))

# Displaying the value
result = square_and_inc1(3)
print(result)
